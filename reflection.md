# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

    There is a settings menu bar on the left side of the app that can be toggled to show/hide. The main screen has the title of the app, and the directions for the chosen difficulty level. There is a input field to enter guesses and buttons to submit guess, restart game and a toggle to show hint.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

    The hints don't work properly. It seems like it doesn't accurately guide the user to guess the correct number as the hints are misleading, for example it hints the user to guess a number outside the bounds of the rules.
    The New game button also doesn't reset the app when you've entered all 8 guesses. It would only reset the number of guesses you had, but all other game state of the UI elements remains unchanged.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  The AI suggested to refactor many of the logic that was located in app.py into the file logic_utils.py, this removed many redundant pieces of code.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  When I came to add some tests for the fixes the AI suggested, there were edits in how the AI was implementing the test cases that didn't make any sense such as testing a function that didn't exist but thought that it should be added when I didn't think it needed to.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I asked the AI to generate the tests for the bug fixes, then I ran the the tests to make sure they passed. Then I booted up the app and manually tested myself to see if the bug still existed in the code.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  I manually tested the new game button to see if it truly did reset the game once I added the fix for this issue. It showed me that we could refactor this particular logic to be included in the logic_utils.py file instead of app.py to reduce clutter in the app.py file.

- Did AI help you design or understand any tests? How?

  The AI was the one that generated the test cases using the description of the fixes I wanted to target. Then I would look over the proposed test cases to make sure they made sense and then determined if the test behaved as they should.


---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

  I didn't experience this bug while I was running the original app. But if this bug was there I would imagine this bug is caused by something that is reseting the state of the game so it is constantly generating new secret numbers.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Streamlit is kind of like a server that is running your app. A session state is like a container that keeps log of all the the statues and variables of the current game that is being updated in real time.

- What change did you make that finally gave the game a stable secret number?

  I didn't run into this bug so I didn't have to make a change to ensure a stable secret number.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

  I want to keep the habbit of honing into specific details when I'm working with an AI agent to make sure I am tackling the problem extensively. Also referencing relevant files so that the AI agent will have more contexts of my prompts.

  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?


  I would maybe try to implement my own fixes and use AI just to try to find where the bugs are. Then I would use AI to check my work and see if what I did made any sense.

- In one or two sentences, describe how this project changed the way you think about AI generated code.


  This project helped me see how AI can help tremendously in writing test cases. But it also taught me to be more cognizant of the suggestions the AI code is making, because sometimes it suggest to do things that are unnecesary.