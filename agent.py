import random
def initialize_environment():
    states=["clean","dirty"]
    current_state=random.choice(states)
    return current_state

def perceive(current_state):
    return current_state

def decide(state):
    if state=="dirty":
        return "clean"
    else:
        return "stay idle"
def act(action,current_state):
    if action=="clean":
        print("cleaning the environment")
        current_state="clean"
    elif action=="stay idle":
        print("staying idle")
    return current_state

def run_agent():
    current_state=initialize_environment()
    for _ in  range(5):
        print(f"current sate:{current_state}")
        
        state=perceive(current_state)
        
        action=decide(state)
        print(f"action chosen:{action}")
        
        current_state=act(action,current_state)
        print("____________")
run_agent()