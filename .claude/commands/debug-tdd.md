Debug failing tests for: $ARGUMENTS

Debugging process:

1. Show me the exact test failure output
2. Identify which specific test(s) are failing
3. Analyze the failure:
   - Is it an assertion error?
   - Is it a runtime exception?
   - Is it a setup/teardown issue?
4. Examine the test logic vs implementation
5. Propose fix (usually to implementation, rarely to test)
6. Apply fix and re-run tests
7. Verify fix doesn't break other tests

Questions to investigate:

- Is the test expectation correct?
- Is the implementation logic flawed?
- Are there missing dependencies or setup?
- Is this an integration vs unit test issue?

Remember: Tests define the contract - fix the code, not the test!
