"""Template for bug regression tests.

Copy this file and rename to test_issue_<number>.py when fixing a bug.
"""

import pytest
# from src.module import function_with_bug


def test_issue_NUMBER_description():
    """Regression test for Issue #NUMBER: [brief description]
    
    Reported behavior: [what was wrong]
    Root cause: [why it was wrong]
    Fix: [what was changed]
    
    Steps to reproduce:
    1. [First step]
    2. [Second step]
    3. [Expected vs actual result]
    """
    # Arrange - Set up the conditions that cause the bug
    # input_data = ...
    
    # Act - Execute the code that had the bug
    # result = function_with_bug(input_data)
    
    # Assert - Verify the bug is fixed
    # assert result == expected_value, "Bug still present: [details]"
    pass  # Remove this when implementing


def test_issue_NUMBER_edge_cases():
    """Test edge cases related to the bug fix."""
    # Test any edge cases discovered during debugging
    pass
