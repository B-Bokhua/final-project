# Final Project

### Description
To summarize this project goes throught the flow and tests these actions
1. add 3 posts, first 2 active and last 1 inactive
2. 1st post is visible for kids, parents and teachers
   - we test if it's visible for kid
3. 2nd post is visible only for parents and teachers
   - we test if it's invisible for kid
   - we test if it's visible for teacher and parent
4. we check if 2nd post was added in posts list
   - test to check if title is present
   - test to check if text is present
   - test to check if background url has changed
5. we test if 3rd post on add listing page has inactive status
---
### Requirements
- selenium 4.26.1
- pytest 8.3.3
- python 3.13
- Google Chrome Version 131.0.6778.86 (Official Build) (x86_64)