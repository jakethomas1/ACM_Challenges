# 🏆 ACM Hackathon – 2nd Place Winner 🏆


Achieved **2nd place** in **ACM at CSUSM**'s first hackathon as a **solo developer**. 

<img src="https://github.com/jakethomas1/ACM_Challenges/blob/main/Screenshot%202025-04-18%20145624.png" width=650>

# Challenge 1: Romans to Numerals 
https://github.com/acm-csusm/hackathon-2025/blob/main/challenge1/roman-to-numeral-readme.md
# Challenge 2: QED Quickly! 
https://github.com/acm-csusm/hackathon-2025/blob/main/challenge2/README.md
# Challenge 3: Speakhard to Speakeasy 
https://github.com/acm-csusm/hackathon-2025/blob/main/challenge3/optimize-english-readme.md
# Challenge 4: I Know a Shortcut! 
https://github.com/acm-csusm/hackathon-2025/blob/main/challenge4/gps-readme.md

# Romans to Numerals

These super bowls number are getting way too long! What does super bowl LX even mean?!

## Your Task

In the most optimal way possible, create a converter for Roman numerals to regular numbers. `I`, `V`, `X`, `L`, `C`, `D` and `M` are the possible digits in a roman numeral. `I` is 1, `V` is 5, `X` is 10, `L` is 50, `C` is 100, `D` is 500, `M` is 1000. 

2 is `II`, 3 is `III`, and so on. However, 4 is `IV`, because V is 5 and 5 - 1 is 4. This subtraction can occur as such:

* `I` before `V` or `I` before `X` making 4 and 9, respectively
* `X` before `L` and `X` before `C` making 40 and 90, respectively.
* `C` before `D` and `C` before `M` making 400 and 900. 

Examples:

1. In: `IV`, out: 4, because 5 - 1 is 4. 
2. In: `LX`, out: 60, because 50 + 10 is 60.
3. In: `XCIX`, out: 99, because 100 - 10 - 1 + 10 is 99. 

Solve as efficiently as possible. Good luck!



# QED Quickly! #

Suppose every odd natural number greater than 1 can be written as the sum of a prime number and 2 times a square as seen below:


### k = p + 2 * (n)^2 ###


Where k is an odd number, p is a prime, and n is some integer. For example:

---

`9 = 7 + 2 * (1)^2`
	
`27 = 19 + 2 * (2)^2`

`43 = 43 + 2 * (0)^2`

`93474253 = 93425581 + 2 * (156)^2`

---

And so on until infinity. We have a sneaking suspicion this might be false and we need you to prove it through contradiction!

## Your Task

Create an algorithm to find as many odd numbers as possible to disprove the above expression. The more numbers you find, the better your score will be!

**Please submit the numbers you believe to contradict this conjecture in a .txt file, see `example.txt` for general formatting.**



# Speakhard to Speakeasy

You've recently been hired by a company. The catch? It's run by defrosted cavemen from the Paleolithic era. They're quite upset with the state of language currently. The CEO, Crug Grood, is aways saying, "Why many word? Less word make easy," while swinging his club about with fervor. 

## Your Task

To make his life easier, create a translator to optimize English, cutting as much as you deem reasonable from the language while still maintaining the meaning of the sentence. Use the following sentences often heard around the office as your inputs:

#### Social Interactions:
**"Allen has mistaken me for his friend Marcus Halberstam. It seems logical because Marcus also works at P&P and in fact does the same exact thing I do and he also has a penchant for Valentino suits and Oliver Peoples glasses. Marcus and I even go to the same barber, although I have a slightly better haircut."**

#### Sales Pitches
**"As you all know, first prize is a Cadillac Eldorado. Anybody wanna see second prize? Second prize's a set of steak knives. Third prize is you're fired."**

#### Budget Talks
**"The good news is Vinnie, you're not going to care cause you're gonna make so much money. That's what I get out of it. Wanna know what you get out of it? You get the ice cream, the hot fudge, the banana and the nuts. Right now I get the sprinkles, and you- if this goes through, I get the cherry. But you get the sundae, Vinny. You get the sundae."**

#### Legal Troubles
**"And I'll bet what you hated the most was that they identified me as a co-founder of Facebook, which I am. You better lawyer up asshole, because I'm not coming back for 30%, I'm coming back for everything."**

#### Fatherly Advice
**"Because the man who makes an appearance in the business world, the man who creates personal interest, is the man who gets ahead. Be liked and you will never want. I never have to wait in line to see a buyer."**

The rules are a bit looser for this challenge; just use your best judgement to make sure Crug Grood understands the above inputs and optimize them as efficiently as possible. There is no one correct answer for either input!

---

Here's an example with a different input:

Input: **"Two little mice fell into a bucket of cream. The first mouse quickly gave up and drown. The second mouse wouldn’t quite. He struggled so hard that eventually he churned that cream into butter and crawled out. Gentlemen, as of this moment, I am that second mouse"**

Output: **"Two small mice fall in big milk. First mouse quit, drown. Second mouse fight, make butter, crawl out. Me second mouse!"**



# I Know a Shortcut!

You're a First year student with an unfortunate schedule. Somehow you got a class in every building on campus: **Science Hall 1, Academic Hall, Markstein Hall, University Hall, Social and Behavioral Science Building, Kellogg Library, Science Hall 2, and Extended Learning Building**. Not only are they all over the place, they're also all on the top floors of each building. Being a first year, you're not crushed by this fact and decide this is the perfect opportunity to find the most perfect route between all the buildings.

## Your Task

Find the **shortest** path between each building that allows you to make it to your classes on time and then back to your starting building within the following constraints:

1. No moving through bushes, barriers, or walls; all nodes must be on walkable paths.

2. all distances have x, y, and z components.

3. Any building can be the starting/ending location, buildings can only be visited once except the starting/ending location. This rule does not apply to builds not listed above

4. Speed and time are negligible, the only variable is distance.

5. Curved distances or stairs can be thought as flat slopes.

6. if some paths are condition dependent, account for the **Expected Value** of the path ie `distance = path_condition * E(x)`. 

## Formatting and Outputs

Collect information to create your shortest path by any means you see fit, try to get accurate information. Your code should output the total distance of your shortest path and print all nodes that are part of the path in order with their distances in meters. Please submit the information in a .txt file, see `example.txt` for an example output.

## Additional map

We would like a marked up map of the path taken between each building be included in your submission, see `map.png` for a reference. Use `Empty.png` for the mark up of your path.
