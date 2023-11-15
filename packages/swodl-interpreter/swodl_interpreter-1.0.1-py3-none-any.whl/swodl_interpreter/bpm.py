import re
import time
import copy
import logging
import multiprocessing as mp
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from swodl_interpreter.runner import Runner
from xml.etree.ElementTree import ElementTree
from pathlib import Path


logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

@dataclass
class Args:
    host = None
    debug = False
    brake_point = []
    check_syntax = False
    show_code = False
    show_args = False
    include_folder = None
    mock = None
    wf_folder = '.'

class Script:
    def __init__(self, process, name, script, inputs, outputs, next, configs):
        self.process = process
        self.name = name
        self.script = script
        self.inputs = inputs
        self.outputs = outputs
        self.next = next
        self.configs = configs
        process.scripts.update({name: None})

    def run(self, loop_index=-1):
        if self.script != '_skip_':
            try:
                with open(Path(self.configs['wf_folder']) / f'{self.script}.wf', 'r') as f:
                    Args.host = self.configs['host']
                    Args.mock = self.configs['mock']
                    Args.include_folder = self.configs['include_folder']
                    Args.wf_folder = self.configs['wf_folder']
                    runner = Runner.from_file(f, Args())
                self.process.scripts.update({self.name: 'Running'})
                pvars = {**self.process.vars,
                        **{'P_TASK_LOOP_NO': loop_index + 1,
                           'P_TASK_LOOP_IND': loop_index}}
                inputs = {wname: pvars.get(pname, None) for wname, pname in self.inputs.items()}
                runner.run(inputs)
                self.process.scripts.update({self.name: 'Finished'})
                scope = runner.interpreter.scope.Global
                self.process.vars.update(
                    {pname: scope.get(wname, None) for wname, pname in self.outputs.items()})
            except Exception as e:
                print(e)
                self.process.scripts.update({self.name: 'Failed'})
        if self.next:
            self.next.run(loop_index)

class Condition:
    def __init__(self, condition, next):
        self.condition = condition
        self.next = next

    def is_true(self):
        return self.condition()

class Decision:
    def __init__(self, conditions):
        self.conditions = conditions
        #self.join = join

    def run(self, loop_index=-1):
        for condition in filter(lambda x: x.condition != 'Default', self.conditions):
            if condition.is_true():
                return condition.next.run(loop_index) if condition.next else None
        return next(filter(lambda x: x.condition == 'Default', self.conditions)).next.run(loop_index)

class Fork:
    def __init__(self, transitions):
        self.transitions = transitions

    def run(self, loop_index=-1):
        processes = []
        #mp.set_start_method('spawn')
        for transition in self.transitions:
            p = mp.Process(target=transition.run, args=(loop_index,))
            processes.append(p)
            p.start()
        for process in processes:
            process.join()
        transition.next.run(loop_index)

class Process:
    def __init__(self, name, vars):
        manager = mp.Manager()
        self.name = name
        self.vars = manager.dict()
        self.vars.update(vars)
        self.scripts = {}

    def set_node(self, node):
        self.node = node

    def run(self, loop_index=-1):
        _next = self.node
        while _next:
            _next = _next.run(loop_index)
            print(self.vars)

class Sub:
    def __init__(self, process, name, subnext, next):
        self.process = process
        self.name = name
        self.next = next
        self.subnext = subnext

    def run(self, loop_index=-1):
        if self.subnext:
            self.subnext.run(loop_index)

class Parallel(Sub):
    def run(self, loop_index=-1):
        processes = []
        if self.subnext:
            for i in range(self.max):
                p = mp.Process(target=self.subnext.run, args=(i,))
                processes.append(p)
                p.start()
            for process in processes:
                process.join()

class Loop(Sub):
    def run(self, loop_index=-1):
        if self.subnext:
            for i in range(self.max):
                self.subnext.run(i)

class Delay:
    def __init__(self, time, next, delay_multiplier):
        self.time = time * delay_multiplier
        self.next = next

    def run(self, loop_index=-1):
        logger.info(f'Sleep {self.time} second')
        time.sleep(self.time)
        if self.next:
            self.next.run(loop_index)

class UserTask:
    def __init__(self, next):
        self.next = next

    def run(self, loop_index=-1):
        print(f'UserTask [index={loop_index}]')
        if self.next:
            self.next.run(loop_index)

class State:
    def __init__(self, text, next):
        self.text = text
        self.next = next

    def run(self, loop_index=-1):
        logger.info(f'[[{self.text}]]')
        if self.next:
            self.next.run(loop_index)

class Error(State):
    def run(self, loop_index=-1):
        logger.error(self.text)
        if self.next:
            self.next.run(loop_index)

def get_activity_type(activity, namespace):
    script = activity.find('./xmlns:Implementation/xmlns:Task/xmlns:TaskScript/xmlns:Script', namespace)
    state = activity.find('./xmlns:NodeGraphicsInfos/xmlns:NodeGraphicsInfo', namespace)
    attribs = {x.attrib['Name']: x.attrib['Value'] for x in activity.findall('.//xmlns:ExtendedAttribute', namespace)}

    if activity.find('./xmlns:Event/xmlns:StartEvent', namespace) != None:
        activity_type = 'start'
    elif activity.find('./xmlns:Event/xmlns:EndEvent', namespace) != None:
        activity_type = 'end'
    elif activity.find('.//xmlns:TriggerTimer', namespace) != None:
        activity_type = 'delay'
    elif script != None and script.text != '':
        activity_type = 'wf'
    elif 'ISCANCEL' in attribs and attribs['ISCANCEL'] == 'True':
        activity_type = 'cancelled'
    elif state != None and state.attrib['FillColor'] == '-478412':
        activity_type = 'state'
    elif state != None and state.attrib['FillColor'] == '-5762532':
        activity_type = 'error'
    elif (activity.find('./xmlns:Route', namespace) != None
        and 'MarkerVisible' in activity.find('./xmlns:Route', namespace).attrib
        and activity.find('./xmlns:Route', namespace).attrib['MarkerVisible'] == 'true'):
        activity_type = 'decision'
    elif (activity.find('./xmlns:ExtendedAttributes/xmlns:ExtendedAttribute[@Name=\'ParallelGatewayType\']', namespace) != None
        and 'Value' in activity.find('./xmlns:ExtendedAttributes/xmlns:ExtendedAttribute[@Name=\'ParallelGatewayType\']', namespace).attrib
        and activity.find('./xmlns:ExtendedAttributes/xmlns:ExtendedAttribute[@Name=\'ParallelGatewayType\']', namespace).attrib['Value'] == 'Fork'):
        activity_type = 'fork'
    elif (activity.find('./xmlns:ExtendedAttributes/xmlns:ExtendedAttribute[@Name=\'ParallelGatewayType\']', namespace) != None
        and 'Value' in activity.find('./xmlns:ExtendedAttributes/xmlns:ExtendedAttribute[@Name=\'ParallelGatewayType\']', namespace).attrib
        and activity.find('./xmlns:ExtendedAttributes/xmlns:ExtendedAttribute[@Name=\'ParallelGatewayType\']', namespace).attrib['Value'] == 'Join'):
        activity_type = 'join'
    elif activity.find('./xmlns:Loop/xmlns:LoopMultiInstance[@MI_Ordering=\'Parallel\']', namespace) != None:
        activity_type = 'parallel'
    elif activity.find('./xmlns:Loop[@LoopType=\'Standard\']', namespace) != None:
        activity_type = 'loop'
    elif activity.find('./xmlns:BlockActivity', namespace) != None:
        activity_type = 'sub'
    elif activity.find('./xmlns:Implementation/xmlns:Task/xmlns:TaskUser', namespace) != None:
        activity_type = 'usertask'
    else:
        activity_type = 'unknown'
    return activity_type

ns = {'xmlns': 'http://www.wfmc.org/2008/XPDL2.1'}

def get_param(process, name):
    sub_xpath = './xmlns:ExtendedAttributes/xmlns:ExtendedAttribute'
    return process \
        .find(f"{sub_xpath}[@Name='{name}']", ns) \
        .attrib['Value']

def get_attrs(process):
    p = process.findall('./xmlns:ExtendedAttributes/xmlns:ExtendedAttribute', ns)
    return {x.attrib['Name']: x.attrib['Value'] for x in p}

a = False
def get_true():
    global a
    if not a:
        a = True
        return False
    return a

class Lifecycle:
    def __init__(self, p, operation, expected, actual) -> None:
        self.p = p
        self.operation = operation
        self.expected = expected
        self.actual = actual

    def evaluate(self) -> bool:
        actual = p.scripts[self.actual]
        if self.operation == '==':
            return self.expected == actual
        elif self.operation == '!=':
            return self.expected != actual
        return False

def get_condition(p, transition):
    condition = transition.find('./xmlns:Condition', ns)
    if condition != None and len(condition.attrib) > 0:
        conditionType = condition.attrib['Type']
        if conditionType == 'CONDITION': # TODO: Add more condition types
            expression = condition.find('./xmlns:Expression', ns).text
            expression_group = re.fullmatch(r'(?P<name>\w+)\.Lifecycle\s*(?P<operation>[=!<>]{1,2})\s*(?P<status>\w+)', expression).groupdict()
            expression = get_true#Lifecycle(p, expression_group["operation"],
                         #       expression_group["status"],
                         #       expression_group["name"]).evaluate
        elif conditionType == 'OTHERWISE':
            expression = 'Default'
        else:
            expression = ''
        return expression

def create_sub(ap, p, activity, _class, next_activity, delay_multiplier, configs):
    sub_activityName = activity.attrib['Name']
    setId = activity.find('.//xmlns:BlockActivity', ns).attrib['ActivitySetId']
    pp = ap.find(f".//xmlns:ActivitySet[@Id='{setId}']", ns)
    loop = activity.find('.//xmlns:LoopStandard', ns) or activity.find('.//xmlns:LoopMultiInstance', ns)
    #sub_process = Process(pp.attrib["Name"], get_attrs(pp))
    sub_activities = pp.findall('./xmlns:Activities/xmlns:Activity', ns)
    sub_transitions = pp.findall('./xmlns:Transitions/xmlns:Transition', ns)
    start_id = [x.attrib['Id'] for x in sub_activities if 'start' == get_activity_type(x, ns)][0]
    next_id = [x.attrib['To'] for x in filter(lambda x: x.attrib['From'] == start_id, sub_transitions)][0]
    sub_next_activity = [x for x in sub_activities if x.attrib['Id'] == next_id][0]
    obj = _class(p,
        sub_activityName,
        parse_activity(ap, p, sub_next_activity, sub_activities, sub_transitions, delay_multiplier, configs),
        next_activity)
    obj.max = 0
    if loop is not None:
        obj.max = int(loop.attrib['LoopMaximum'])
    return obj

def parse_activity(ap, p, activity, activities, transitions, delay_multiplier, configs):
    activityName = activity.attrib['Name']
    activity_type = get_activity_type(activity, ns)
    next_ids = [x for x in filter(lambda x: x.attrib['From'] == activity.attrib['Id'], transitions)]
    next_activities = [x for x in activities if x.attrib['Id'] in [y.attrib['To'] for y in next_ids]]
    if 'state' == activity_type:
        return State(activityName, parse_activity(ap, p, next_activities[0], activities, transitions, delay_multiplier, configs))
    elif 'error' == activity_type:
        return Error(activityName, parse_activity(ap, p, next_activities[0], activities, transitions, delay_multiplier, configs))
    elif 'wf' == activity_type:
        mappings = activity.find('.//xmlns:ExtendedAttribute[@Name="MAPPINGS"]', ns)
        if mappings != None:
            mappings = mappings.attrib['Value']
            mappingsTree = ET.fromstring(mappings)
            inputs = mappingsTree.findall('.//Input')
            inputs = {x.attrib['var']: x.attrib['from'] if 'from' in x.attrib else x.text for x in inputs}
            outputs = mappingsTree.findall('.//Output')
            outputs = {x.attrib['from']: x.attrib['property'] for x in outputs}
        return Script(p,
            activity.attrib['Name'],
            activity.find('.//xmlns:Script', ns).text,
            inputs,
            outputs,
            parse_activity(ap, p, next_activities[0], activities, transitions, delay_multiplier, configs),
            configs)
    elif 'decision' == activity_type:
        return Decision([Condition(get_condition(p, next(filter(lambda y: y.attrib['To'] == x.attrib['Id'], transitions))),
            parse_activity(ap, p, x, activities, transitions, delay_multiplier, configs)) for x in next_activities])
    elif 'fork' == activity_type:
        return Fork([parse_activity(ap, p, x, activities, transitions, delay_multiplier, configs) for x in next_activities])
    elif 'join' == activity_type:
        return parse_activity(ap, p, next_activities[0], activities, transitions, delay_multiplier, configs)
    elif 'end' == activity_type:
        return None
    elif 'cancelled' == activity_type: # TODO: Change to cancelled
        return parse_activity(ap, p, next_activities[0], activities, transitions, delay_multiplier, configs)
    elif 'parallel' == activity_type:
        return create_sub(ap, p, activity, Parallel, parse_activity(ap, p, next_activities[0], activities, transitions, delay_multiplier, configs), delay_multiplier, configs)
    elif 'sub' == activity_type:
        return create_sub(ap, p, activity, Sub, parse_activity(ap, p, next_activities[0], activities, transitions, delay_multiplier, configs), delay_multiplier, configs)
    elif 'loop' == activity_type:
        return create_sub(ap, p, activity, Loop, parse_activity(ap, p, next_activities[0], activities, transitions, delay_multiplier, configs), delay_multiplier, configs)
    elif 'usertask' == activity_type:
        return UserTask(parse_activity(ap, p, next_activities[0], activities, transitions, delay_multiplier, configs))
    elif 'delay' == activity_type:
        return Delay(int(re.match(r'\d+', activity.find('.//xmlns:TriggerTimer', ns).attrib['TimeCycle'])[0]),
            parse_activity(ap, p, next_activities[0], activities, transitions, delay_multiplier, configs),
            delay_multiplier)
    else:
        print(activity_type)

def parse(path, inputs={}, delay_multiplier=1, args=None):
    manager = mp.Manager()
    configs = manager.dict()
    if args is not None:
        configs['host'] = args._host
        configs['mock'] = args._mock
        configs['include_folder'] = args._include_folder
        configs['wf_folder'] = args._wf_folder
    tree = ElementTree()
    tree.parse(path)
    process_node = tree.find(f'.//xmlns:WorkflowProcess/xmlns:Activities[xmlns:Activity]/..', ns)
    process = Process(process_node.attrib['Name'], {**get_attrs(process_node), **inputs})
    activities = process_node.findall('./xmlns:Activities/xmlns:Activity', ns)
    transitions = process_node.findall('./xmlns:Transitions/xmlns:Transition', ns)
    start_id = [x.attrib['Id'] for x in activities if 'start' == get_activity_type(x, ns)][0]
    #end_id = [x.attrib["Id"] for x in activities if "end" == get_activity_type(x, ns)][0]
    next_id = [x.attrib['To'] for x in filter(lambda x: x.attrib['From'] == start_id, transitions)][0]
    next_activity = [x for x in activities if x.attrib['Id'] == next_id][0]
    process.set_node(parse_activity(tree, process, next_activity, activities, transitions, delay_multiplier, configs))
    return process
    #TODO: Add sub process parsing
    # for transition in transitions:
    #     transition_from = transition.attrib['From']
    #     transition_to = transition.attrib['To']
    #     expression = transition.find("./xmlns:Condition/xmlns:Expression", ns)


if __name__ == '__main__':
    p = parse('./tests/bpm.xpdl', {'SomeInDMAttr': 123})
    p.run()
