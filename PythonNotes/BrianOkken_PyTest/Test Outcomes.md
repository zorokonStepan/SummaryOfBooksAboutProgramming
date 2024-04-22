```
    • PASSED (.) — The test ran successfully.
    • FAILED (F) — The test did not run successfully.
    • SKIPPED (s) — The test was skipped. 
                    You can tell pytest to skip a test by using either the @pytest.mark.skip() or @pytest.mark.skipif() 
                    decorators
    • XFAIL (x) — The test was not supposed to pass, and it ran and failed.
                  You can tell pytest that a test is expected to fail by using the @pytest.mark.xfail() decorator.
    • XPASS (X) — The test was marked with xfail, but it ran and passed.
    • ERROR (E) — An exception happened either during the execution of a fixture or hook function, and not during the 
                  execution of a test function. 
```