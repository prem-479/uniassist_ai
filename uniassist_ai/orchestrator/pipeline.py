from uniassist_ai.agents.router_agent import RouterAgent

def main():
    router = RouterAgent()

    while True:
        user_input = input("Ask something → ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Exiting.")
            break

        reply = router.route(user_input)
        print("\n" + reply + "\n")

if __name__ == "__main__":
    main()
