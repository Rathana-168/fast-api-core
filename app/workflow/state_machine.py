from transitions.extensions.asyncio import AsyncMachine
import asyncio

class AsyncBaseTransition:
    initial = 'init'
    states = ['init', 'next_state']
    transitions = []

    def __init__(self):
        self.machine = AsyncMachine(
            model=self,
            initial=self.initial,
            states=self.states,
            transitions=self.transitions,
            send_event=True,
            auto_transitions=True,
            before_state_change=[self._before_state_change],
            after_state_change=[self._after_state_change],
            on_exception=[self._on_exception]
        )

    @staticmethod
    def _before_state_change(event):
        print(event)
        print("I do before state change")

    @staticmethod
    def _after_state_change(event):
        # raise Exception('Error')
        print("I do after state change")

    @staticmethod
    def _on_exception(event):
        print(event)
        print("I will log the exceptions")


x = AsyncBaseTransition()
asyncio.get_event_loop().run_until_complete(x.to_next_state(x=1))

