# Contributing guidelines

## Before contributing

Welcome to [Daily Coding Problem Solutions](https://github.com/ruppysuppy/Daily-Coding-Challenge-Solutions)!
Before sending your pull requests, make sure that you read the whole guidelines.

## Contributing

### Contributor

Thankyou for considering improvising the solutions in this repository! Being one of our
contributors, you agree and confirm that:

-   Your work will be distributed under [MIT License](LICENSE.md) once your pull
    request is merged.
-   You submitted work fulfills the styles and standards of this repository.

### Contribution

Any contribution, from fixing a grammatical errors in a comment to improvising current
solutions is appriciated.

**New implementation** is welcome as long as the solution improvises the
`Time Complexity` and/or `Space Complexity` without deteriorating the either of them
compared to the current solution. But **identical implementation** of an existing
solution will not be accepted.

**Improving comments** are also highly welcome. But **fake pull requests**, like
_unnecessarily changing the wording, adding 'a' or 'the', etc_ are highly discouraged.
Such pull requests will be closed immediately and labeled as `invalid`.

### Other Requirements for Submissions

-   Use [black](https://pypi.org/project/black/) to format you code.
-   Strictly use **PascalCase** for class names and **snake_case** in your variable and
    function names.
-   If you have modified/added documentation work, ensure your language is concise and
    contains no grammatical errors.
-   If you have modified/added code work, make sure the code compiles before
    submitting.
-   Make sure to add
    [**Python type hints**](https://docs.python.org/3/library/typing.html) to all
    functions and methods.
-   Make sure to follow this pattern for any solution:

    ```python
    """
    Problem:

    <Problem Statement>
    """

    # ...
    # necessary functions
    # ...


    if __name__ == "__main__":
        # an example for the solution


    """
    SPECS:

    <time & space complexity>
    """
    ```

-   Most importantly,
    -   **Be consistent in the use of these guidelines when submitting.**
    -   Happy coding!
