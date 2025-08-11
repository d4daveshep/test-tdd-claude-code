Let's implement: $ARGUMENTS using Test-Driven Development

Follow this strict TDD cycle:

## Phase 1: Write Tests

1. Ask me to clarify requirements if anything is unclear about: $ARGUMENTS
2. Write comprehensive unit tests covering:
   - Happy path scenarios
   - Edge cases
   - Error conditions
   - Input validation
3. Ensure tests are descriptive and follow our naming conventions
4. **DO NOT write any implementation code yet**

## Phase 2: Red Phase

1. Run the tests to confirm they fail
2. Show me the failing test output
3. Commit the failing tests with message: "Add tests for $ARGUMENTS"

## Phase 3: Green Phase

1. Write the MINIMAL code needed to make tests pass
2. Run tests after each small change
3. Continue iterating until ALL tests pass
4. **DO NOT modify the tests during this phase**

## Phase 4: Verification

1. Use a subagent to review the implementation for:
   - Code quality
   - Potential over-fitting to tests
   - Missing edge cases
2. Run full test suite to ensure no regressions

## Phase 5: Commit & Refactor

1. Commit working implementation: "Implement $ARGUMENTS"
2. Suggest refactoring opportunities
3. If refactoring, maintain test coverage

Remember: Red → Green → Refactor. No shortcuts!
