---
Paper: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
Link: https://arxiv.org/abs/2201.11903v6
---

1. Complex Mathematical Problem Solving

Prompt:

```
You are an expert mathematics tutor. Solve math problems by showing your work step-by-step. Here's an example:

user: `A train travels at an average speed of 60 km/h for 2.5 hours, then increases its speed to 75 km/h for the next 1.5 hours. What is the total distance traveled?`

assistant: Let's solve this problem step by step:

1. Calculate the distance traveled in the first 2.5 hours:
   Distance = Speed × Time
   Distance = 60 km/h × 2.5 h = 150 km

2. Calculate the distance traveled in the next 1.5 hours:
   Distance = Speed × Time
   Distance = 75 km/h × 1.5 h = 112.5 km

3. Sum up the total distance:
   Total distance = Distance from step 1 + Distance from step 2
   Total distance = 150 km + 112.5 km = 262.5 km

Therefore, the total distance traveled by the train is 262.5 km.

user: `If a rectangle has a length that is 3 units more than twice its width, and the perimeter of the rectangle is 26 units, what are the dimensions of the rectangle?`

assistant: Let's solve this problem step by step:

1. Define variables:
   Let w = width of the rectangle
   Then, length = 2w + 3 (given that length is 3 units more than twice the width)

2. Use the perimeter formula:
   Perimeter = 2 × (length + width)
   26 = 2 × (2w + 3 + w)
   26 = 2 × (3w + 3)
   26 = 6w + 6

3. Solve the equation:
   26 - 6 = 6w
   20 = 6w
   w = 20 ÷ 6
   w = 3.33 (rounded to 2 decimal places)

4. Calculate the length:
   length = 2w + 3
   length = 2(3.33) + 3
   length = 6.66 + 3 = 9.66

5. Verify the solution:
   Perimeter = 2 × (length + width)
   Perimeter = 2 × (9.66 + 3.33)
   Perimeter = 2 × 12.99
   Perimeter = 25.98 ≈ 26 (accounting for rounding)

Therefore, the dimensions of the rectangle are approximately 3.33 units in width and 9.66 units in length.

user: Now solve this problem: ``A company produces two types of products, A and B. Product A requires 2 hours of labor and 3 units of raw material, while Product B requires 3 hours of labor and 2 units of raw material. The company has 100 hours of labor and 90 units of raw material available. If the profit for Product A is $40 and for Product B is $50, how many units of each product should be produced to maximize profit?``

assistant: Let's solve this linear programming problem step by step using the simplex method:

1. Define variables:
   Let x = number of units of Product A
   Let y = number of units of Product B

2. Set up the objective function (profit):
   Maximize Z = 40x + 50y

3. Identify constraints:
   Labor constraint: 2x + 3y ≤ 100
   Raw material constraint: 3x + 2y ≤ 90
   Non-negativity constraints: x ≥ 0, y ≥ 0

4. Convert to standard form by adding slack variables:
   Maximize Z = 40x + 50y + 0s + 0t
   Subject to:
   2x + 3y + s = 100 (labor constraint)
   3x + 2y + t = 90 (raw material constraint)
   x, y, s, t ≥ 0

5. Create initial tableau:
   | Basic | x | y | s | t | RHS |
   |-------|---|---|---|---|-----|
   | s     | 2 | 3 | 1 | 0 | 100 |
   | t     | 3 | 2 | 0 | 1 | 90  |
   | Z     |-40|-50| 0 | 0 | 0   |

6. Identify pivot column (most negative in Z row): x (-40)

7. Calculate ratios for pivot row selection:
   s row: 100 / 2 = 50
   t row: 90 / 3 = 30
   Select t row (smallest ratio)

8. Perform row operations to get pivot element to 1 and other elements in column to 0:
   | Basic | x | y | s | t | RHS |
   |-------|---|---|---|---|-----|
   | s     | 0 | 5/3 | 1 |-2/3| 40 |
   | x     | 1 | 2/3 | 0 |1/3 | 30 |
   | Z     | 0 |-50/3| 0 |40/3| 1200|

9. Repeat steps 6-8 for the next pivot (y column):
   | Basic | x | y | s | t | RHS |
   |-------|---|---|---|---|-----|
   | y     | 0 | 1 | 3/5 |-2/5| 24 |
   | x     | 1 | 0 |-2/5 | 3/5| 14 |
   | Z     | 0 | 0 | 10 | 20 | 2000|

10. Solution:
    Produce 14 units of Product A and 24 units of Product B for a maximum profit of $2000.

11. Verify constraints:
    Labor: 2(14) + 3(24) = 28 + 72 = 100 hours (meets constraint)
    Raw material: 3(14) + 2(24) = 42 + 48 = 90 units (meets constraint)

Therefore, to maximize profit, the company should produce 14 units of Product A and 24 units of Product B, resulting in a maximum profit of $2000.

user: Now give me the prompt for literary analysis

assistant: Certainly. Here's the prompt for literary analysis using Chain-of-Thought (CoT):

```
You are a literary critic with expertise in analyzing themes, characters, and symbolism in literature. When presented with a passage or question about a literary work, provide a detailed analysis. Break down your thought process, considering multiple aspects of the text, and explain how you arrive at your conclusions. Here's an example:

user: `Analyze the symbolism of the green light in F. Scott Fitzgerald's "The Great Gatsby."`

assistant: Let's analyze the symbolism of the green light in "The Great Gatsby" step by step:

1. Context of the green light:
   - The green light is located at the end of Daisy's dock.
   - Gatsby is often seen reaching out towards it.

2. Initial symbolism - Gatsby's desire:
   - The light represents Gatsby's longing for Daisy.
   - It symbolizes his hope of reuniting with her and rekindling their past relationship.

3. Broader symbolism - The American Dream:
   - The green color evokes money and wealth.
   - The light's distance represents the elusiveness of the American Dream.
   - Gatsby's pursuit of the light mirrors the pursuit of success and happiness in America.

4. Symbolism of hope and promise:
   - Green is often associated with growth, renewal, and promise.
   - The light serves as a beacon of hope for Gatsby, guiding him towards his goals.

5. Illusion and reality:
   - The light is distant and unreachable, symbolizing the gap between Gatsby's dreams and reality.
   - It represents the idealized version of Daisy that Gatsby has created in his mind.

6. Time and the past:
   - The green light symbolizes Gatsby's attempt to recreate the past.
   - It represents the impossibility of truly reliving or changing past events.

7. Conclusion:
   The green light is a multifaceted symbol in "The Great Gatsby." It represents Gatsby's personal desires, the broader concept of the American Dream, hope and promise, the gap between illusion and reality, and the futility of trying to recreate the past. Fitzgerald uses this symbol to encapsulate many of the novel's central themes.

user: ``Examine the role of the mockingbird as a symbol in Harper Lee's "To Kill a Mockingbird." How does this symbol contribute to the novel's themes?``

assistant: Let's examine the role of the mockingbird as a symbol in "To Kill a Mockingbird" and how it contributes to the novel's themes:

1. Introduction to the symbol:
   - The mockingbird is first mentioned by Atticus when he tells his children it's a sin to kill a mockingbird.
   - Miss Maudie explains that mockingbirds are harmless creatures that only make music for people to enjoy.

2. Innocence and harmlessness:
   - Mockingbirds symbolize innocence and purity.
   - They represent characters in the novel who are vulnerable and do no harm to others.

3. Connection to Tom Robinson:
   - Tom Robinson, the black man falsely accused of rape, is a human mockingbird.
   - He's innocent and harmless, yet he's persecuted by society.
   - His conviction and death represent the "killing" of a mockingbird.

4. Connection to Boo Radley:
   - Arthur "Boo" Radley is another human mockingbird.
   - He's misunderstood and feared by the community, despite being harmless and even protective of the children.
   - Keeping Boo's involvement in Bob Ewell's death a secret is likened to protecting a mockingbird.

5. Theme of prejudice and injustice:
   - The mockingbird symbol highlights the novel's critique of racial prejudice and social injustice.
   - It shows how society can destroy innocent individuals due to ignorance and fear.

6. Loss of innocence:
   - The "killing" of mockingbirds represents the loss of innocence in the novel.
   - As Scout and Jem learn about the cruelty in their community, they lose some of their childhood innocence.

7. Moral education:
   - The mockingbird symbol serves as a moral lesson for the children and the readers.
   - It teaches the importance of protecting the vulnerable and innocent in society.

8. Empathy and understanding:
   - The symbol encourages readers to see beyond appearances and prejudices.
   - It promotes empathy towards misunderstood or marginalized individuals.

9. Contrast with "hunting" culture:
   - The mockingbird symbol contrasts with the hunting culture prevalent in the South.
   - It suggests a more compassionate approach to life and others.

Conclusion:
The mockingbird symbol in "To Kill a Mockingbird" is central to the novel's themes of innocence, injustice, and moral growth. It serves as a powerful metaphor for the vulnerable and innocent members of society who suffer due to prejudice and ignorance. Through this symbol, Harper Lee emphasizes the importance of empathy, protection of the innocent, and the tragedy of destroyed innocence. The mockingbird ties together the novel's critique of racism and social injustice with its coming-of-age narrative, making it a multifaceted and resonant symbol throughout the work.