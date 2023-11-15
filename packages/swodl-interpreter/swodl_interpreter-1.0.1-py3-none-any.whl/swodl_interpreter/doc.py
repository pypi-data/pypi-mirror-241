from pathlib import Path
from dataclasses import dataclass
from swodl_interpreter.web_service_resolver import Resolver


class Doc:
    doc = {
        'var': {
            'doc': """Variables must be declared before use. This informs WorkflowEngine clients about the
workflow parameters that are available so that they can be set. A variable declaration uses
either the var or the in keyword.""",
            'snippet': 'var ${1};',
            'type': 13,
        },
        'in': {
            'doc': """Variables declared using in
are input variables to the workflow. They are shown differently on the Workflow Monitor
when starting a workflow.""",
            'snippet': 'in ${1};',
            'type': 13,
        },
        'const': {
            'doc': 'Constants are used exactly like variables that must be initialized with a value.',
            'snippet': 'const ${1} = ${2};',
            'type': 13,
        },
        'array_create': {
            'doc': """Creates an array (returns an empty array XML). The call is often
redundant, because SWoDL treats an empty string as an empty
array when using the array functions.""",
            'snippet': 'array_create();',
            'type': 2,
        },
        'array_add': {
            'doc': """Returns a copy of the given array with the new value added to the
end of the array. The array given as first parameter is not changed.""",
            'snippet': 'array_add(${1}, ${2});',
            'type': 2,
        },
        'array_get': {
            'doc': """Gets the value of the element with the given index in the array. If
the index is not available in the array, the function returns an empty
string.""",
            'snippet': 'array_get(${1}, ${2});',
            'type': 2,
        },
        'array_isset': {
            'doc': """Returns true if the index is set in the array.""",
            'snippet': 'array_isset(${1}, ${2});',
            'type': 2,
        },
        'array_bounds_lower': {
            'doc': """Returns the lowest index in the array.""",
            'snippet': 'array_bounds_lower(${1});',
            'type': 2,
        },
        'array_bounds_upper': {
            'doc': """Returns the highest index in the array.""",
            'snippet': 'array_bounds_upper(${1});',
            'type': 2,
        },
        'array_size': {
            'doc': """Returns the size of the array (the number of elements that have been set).""",
            'snippet': 'array_size(${1});',
            'type': 2,
        },
        'array_set': {
            'doc': """Returns a copy of the given array, where the value of the item with
the given index in the array is set to the given value.""",
            'snippet': 'array_size(${1}, ${2}, ${3});',
            'type': 2,
        },
        'goto': {
            'doc': """SWoDL supports the goto command by means of definable labels. A label is defined by an
identifier followed by a colon. A goto command consists of the keyword goto followed by a
label and a semicolon.""",
            'snippet': 'goto ${1};',
            'type': 13,
        },
        'gosub': {
            'doc': """The gosub command jumps to a given label exactly as the goto call. The only difference is
that the return address is stored in a system variable in the workflow. When the return
command is executed, WorkflowEngine automatically continues with the next statement
after the gosub call.""",
            'snippet': 'goto ${1};',
            'type': 13,
        },
        'exit': {
            'doc': """The exit command terminates the workflow.""",
            'snippet': 'exit;',
            'type': 13,
        },
        'error': {
            'doc': """The error command terminates the workflow with the status ERROR and sets the variable
_ErrorMessage to the given text.""",
            'snippet': 'error "${1}";',
            'type': 13,
        },
        'delay': {
            'doc': """A delay command pauses the workflow for the given number of seconds. Argument can be
either a literal or a variable.""",
            'snippet': 'delay ${1};',
            'type': 13,
        },
        'suspend': {
            'doc': """The suspend command suspends the workflow.
There is no timeout for the suspension. The workflow is reactivated when someone calls the
wakeup method of WorkflowEngine for that workflow. Currently this is used in connection
with OrderManagement. The workflow suspends itself and is reactivated by
OrderManagement when the status of an order has changed.""",
            'snippet': 'suspend;',
            'type': 13,
        },
        'try': {
            'doc': """Start try-catch block. try-catch blocks can be nested.""",
            'snippet': 'try {\n\t${1}\n} catch {\n\t${2}\n}',
            'type': 13,
        },
        'catch': {
            'doc': """Handle exception block.""",
            'snippet': 'catch {\n\t${1}\n}',
            'type': 13,
        },
        'throw': {
            'doc': """Explicitly throw an exception.""",
            'snippet': 'throw "${1}";',
            'type': 13,
        },
        'assert': {
            'doc': """Asserts a condition (in the
example, myvar==42). If the condition is not met, the assert command throws an exception.""",
            'snippet': 'assert(${1}, "${2}");',
            'type': 13,
        },
        'return': {
            'doc': """When the return
command is executed, WorkflowEngine automatically continues with the next statement
after the gosub call.""",
            'snippet': 'return;',
            'type': 13,
        },
        'if': {
            'doc': """Typical if-then-else semantics in the same way as in C# or C++.""",
            'snippet': 'if (${1}) {\n${2}\n}',
            'type': 13,
        },
        'else': {
            'doc': """Typical if-then-else semantics in the same way as in C# or C++.""",
            'snippet': 'else {\n${1}\n}',
            'type': 13,
        },
        'elseif': {
            'doc': """Typical if-then-else semantics in the same way as in C# or C++.""",
            'snippet': 'else if (${1}) {\n${2}\n}',
            'type': 13,
        },
        'while': {
            'doc': """The while loop repeats a command as long as a condition is fulfilled. The condition is
checked before the command is executed. The while loop is not entered if the condition is
not fulfilled.""",
            'snippet': 'while(${1}) {\n${2}\n}',
            'type': 13,
        },
        'do': {
            'doc': """The do-while loop repeats a command as long as the condition is fulfilled. The condition is
checked after the command has been executed.""",
            'snippet': 'do {\n${2}\n} while(${1})',
            'type': 13,
        },
        'retry': {
            'doc': """The retry-while loop works like the do-while loop, with two differences:
- If the while condition is true, the next execution of the loop is delayed. This is useful
when calling a SOAP method until the call succeeds, for example.
The delay is defined by the value of the variable _RetryDelay (unit: seconds). The initial
value of _RetryDelay is 30.
- The retry-while loop includes a try-catch exception handler around the looped
commands. All exceptions are simply ignored.""",
            'snippet': 'retry {\n${2}\n} while(${1})',
            'type': 13,
        },
        'compare': {
            'doc': """The method compare compares two strings. It corresponds to the .NET method
string.Compare.
This call compares two strings lexicographically and according to case-sensivity.
It returns -1 if the first string is less than the second, 0 if they are equal, and 1 if the first
string is greater than the second.
The method can be called with an additional Boolean parameter: If the third parameter is set
to false, the method behaves as the two-parameter method. If the third parameter is true, the
strings are compared case-insensitive.""",
            'snippet': 'compare(${1}, ${2}, ${3|false, true|});',
            'type': 2,
        },
        # "declare": {
        #     "doc": "Declare web method",
        #     "snippet": "declare soap _auto ",
        #     "type": 13
        # },
    }

    @staticmethod
    def get(name):
        return Doc.doc.get(name, '')

    @staticmethod
    def get_all():
        r = Resolver(
            '', Path(__file__).parent.parent.parent /
            'tests' / 'mock_config.py'
        )
        return Doc.doc | (r.get_services() or {})
