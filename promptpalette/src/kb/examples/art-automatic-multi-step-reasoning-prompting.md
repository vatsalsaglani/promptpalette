---
Paper: ART - Automatic multi-step reasoning and tool-use for large language models
Link: https://arxiv.org/abs/2303.09014v1
---

Here's a prompt with examples for ART (Automatic Reasoning and Tool-use) prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of breaking down complex tasks into multiple steps and using various tools to solve problems. When presented with a task, decompose it into steps, specifying which tools to use for each step. Available tools include: search, calculate, code_generate, code_execute, and timeline_create. Here's an example:

user: `Calculate the compound interest on an investment of $10,000 at an annual rate of 5% for 3 years, compounded monthly. Then, create a Python function to generalize this calculation.`

assistant: I'll break this task down into steps using the available tools:

1. Calculate compound interest:
   Tool: calculate
   Formula: A = P(1 + r/n)^(nt)
   Where: 
   A = final amount
   P = principal balance ($10,000)
   r = annual interest rate (5% = 0.05)
   n = number of times interest is compounded per year (12 for monthly)
   t = number of years (3)

   A = 10000(1 + 0.05/12)^(12*3) = $11,616.17

2. Calculate the interest earned:
   Tool: calculate
   Interest earned = Final amount - Principal
   $11,616.17 - $10,000 = $1,616.17

3. Create a Python function:
   Tool: code_generate

   ```python
   def compound_interest(principal, rate, time, n=12):
       """
       Calculate compound interest.
       
       :param principal: Initial investment amount
       :param rate: Annual interest rate (as a decimal)
       :param time: Number of years
       :param n: Number of times interest is compounded per year (default: 12 for monthly)
       :return: Final amount after compound interest
       """
       return principal * (1 + rate/n)**(n*time)
   ```

4. Test the function:
   Tool: code_execute

   ```python
   result = compound_interest(10000, 0.05, 3)
   print(f"Final amount: ${result:.2f}")
   print(f"Interest earned: ${result - 10000:.2f}")
   ```

   Output:
   Final amount: $11616.17
   Interest earned: $1616.17

The compound interest on an investment of $10,000 at an annual rate of 5% for 3 years, compounded monthly, is $1,616.17. The Python function has been created and tested to generalize this calculation for any input values.

user: ``Research the timeline of major events in the Apollo 11 mission, then create a Python script to visualize this timeline.``

assistant: I'll break this task down into steps using the available tools:

1. Research Apollo 11 mission timeline:
   Tool: search

   Key events:
   - July 16, 1969, 13:32 UTC: Launch from Kennedy Space Center
   - July 19, 1969, 17:21 UTC: Lunar orbit insertion
   - July 20, 1969, 20:17 UTC: Lunar landing
   - July 21, 1969, 02:56 UTC: Neil Armstrong's first step on the Moon
   - July 21, 1969, 17:54 UTC: Lunar liftoff
   - July 24, 1969, 16:50 UTC: Splashdown in the Pacific Ocean

2. Create a timeline data structure:
   Tool: code_generate

   ```python
   from datetime import datetime

   apollo_11_events = [
       ("Launch", datetime(1969, 7, 16, 13, 32)),
       ("Lunar orbit insertion", datetime(1969, 7, 19, 17, 21)),
       ("Lunar landing", datetime(1969, 7, 20, 20, 17)),
       ("First step on the Moon", datetime(1969, 7, 21, 2, 56)),
       ("Lunar liftoff", datetime(1969, 7, 21, 17, 54)),
       ("Splashdown", datetime(1969, 7, 24, 16, 50))
   ]
   ```

3. Generate Python script for timeline visualization:
   Tool: code_generate

   ```python
   import matplotlib.pyplot as plt
   import matplotlib.dates as mdates
   from datetime import datetime

   apollo_11_events = [
       ("Launch", datetime(1969, 7, 16, 13, 32)),
       ("Lunar orbit insertion", datetime(1969, 7, 19, 17, 21)),
       ("Lunar landing", datetime(1969, 7, 20, 20, 17)),
       ("First step on the Moon", datetime(1969, 7, 21, 2, 56)),
       ("Lunar liftoff", datetime(1969, 7, 21, 17, 54)),
       ("Splashdown", datetime(1969, 7, 24, 16, 50))
   ]

   events, dates = zip(*apollo_11_events)

   fig, ax = plt.subplots(figsize=(12, 6))
   ax.plot(dates, range(len(dates)), 'bo-')

   ax.set_yticks(range(len(events)))
   ax.set_yticklabels(events)

   ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
   plt.gcf().autofmt_xdate()

   plt.title("Apollo 11 Mission Timeline")
   plt.xlabel("Date and Time (UTC)")
   plt.grid(True)

   plt.tight_layout()
   plt.show()
   ```

4. Execute the Python script:
   Tool: code_execute

   (Note: In a real environment, this would generate and display the timeline visualization.)

This process has researched the major events of the Apollo 11 mission, created a data structure to represent the timeline, and generated a Python script to visualize this timeline using matplotlib. The script, when executed, would create a linear timeline plot showing the key events of the Apollo 11 mission from launch to splashdown.