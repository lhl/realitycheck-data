# matplotlib/matplotlib Issue #31130: [MNT] Switch from `np.column_stack()` to `np.vstack().T` for performance
- **Source**: https://github.com/matplotlib/matplotlib/issues/31130
- **Retrieved (UTC)**: 2026-02-20T05:57:37Z
- **state**: closed
- **created_at**: 2026-02-10T21:53:30Z
- **updated_at**: 2026-02-13T05:33:54Z
- **closed_at**: 2026-02-11T10:46:33Z
- **Participants (unique)**: scottshambaugh, github-actions[bot], timhoffm, anntzer, jklymak, Borda, story645

## Body
> From the discussion in https://github.com/matplotlib/matplotlib/pull/31001#discussion_r2790413429, it looks like `np.column_stack()` is generally a slow operation compared to `np.vstack().T`. This is because the former has to interleave elements in memory whereas the second does contiguous memory copies and returns a view.
>
> It's unclear to me how many of these operations are driving time spent in the hot paths of the code, but we should see a performance improvement by switching things over.
>
> Marking this as an easy first issue since it's largely a find-and-replace.
>
> ```
> 10,000 elements: 10 runs x 10,000 iterations
>
> With broadcast:
> - `np.column_stack(np.broadcast_arrays(x, y))`: 36.47 us
> - `np.vstack(np.broadcast_arrays(x, y)).T`: 27.67 us
> - `np.empty + assign`: 30.09 us
>
> Without broadcast:
> - `np.column_stack([x, y])`: 20.63 us
> - `np.vstack((x, y)).T`: 13.18 us
> ```
>
> ```python
> """Benchmark different array combination methods."""
>
> import timeit
> import numpy as np
>
> N = 10_000
> NUMBER = 10_000
> REPEAT = 10
>
> x = np.linspace(0, 1, N)
> y = np.float64(2.0)
>
> # Pre-matched arrays for non-broadcast cases
> x_full = x
> y_full = np.full(N, 2.0)
>
>
> def broadcast_column_stack():
>     return np.column_stack(np.broadcast_arrays(x, y))
>
> def broadcast_vstack_T():
>     return np.vstack(np.broadcast_arrays(x, y)).T
>
> def broadcast_empty_assign():
>     out = np.empty((N, 2))
>     bx, by = np.broadcast_arrays(x, y)
>     out[:, 0] = bx
>     out[:, 1] = by
>     return out
>
> def no_broadcast_column_stack():
>     return np.column_stack([x_full, y_full])
>
> def no_broadcast_vstack_T():
>     return np.vstack((x_full, y_full)).T
>
>
> def bench(func):
>     times = timeit.repeat(func, number=NUMBER, repeat=REPEAT)
>     return min(times) / NUMBER
>
>
> if __name__ == "__main__":
>     print(f"{N:,} elements: {REPEAT} runs x {NUMBER:,} iterations")
>
>     broadcast_cases = [
>         ("np.column_stack(np.broadcast_arrays(x, y))", broadcast_column_stack),
>         ("np.vstack(np.broadcast_arrays(x, y)).T", broadcast_vstack_T),
>         ("np.empty + assign", broadcast_empty_assign),
>     ]
>
>     no_broadcast_cases = [
>         ("np.column_stack([x, y])", no_broadcast_column_stack),
>         ("np.vstack((x, y)).T", no_broadcast_vstack_T),
>     ]
>
>     print("\nWith broadcast:")
>     for label, func in broadcast_cases:
>         t = bench(func)
>         print(f"- `{label}`: {t * 1e6:.2f} us")
>
>     print("\nWithout broadcast:")
>     for label, func in no_broadcast_cases:
>         t = bench(func)
>         print(f"- `{label}`: {t * 1e6:.2f} us")
> ```

## Comments

### Comment 1: github-actions[bot] (2026-02-10T21:54:38Z)
> ### Good first issue - notes for new contributors
>
> This issue is suited to new contributors because it does not require understanding of the
> Matplotlib internals. To get started, please see our [contributing
> guide](https://matplotlib.org/stable/devel/index).
>
> **We do not assign issues**. Check the *Development* section in the sidebar for linked pull
> requests (PRs). If there are none, feel free to start working on it. If there is an open PR, please
> collaborate on the work by reviewing it rather than duplicating it in a competing PR.
>
> If something is unclear, please reach out on any of our [communication
> channels](https://matplotlib.org/stable/devel/contributing.html#get-connected).

### Comment 2: scottshambaugh (2026-02-10T21:57:04Z)
> Hid one automatically generated comment from @AiGentsy. This is a low priority, easier task which is better used for human contributors to learn how to contribute.

### Comment 3: timhoffm (2026-02-11T07:54:18Z)
> In a quick test
>
> <details>
>
> <summary>Code</summary>
>
> ```python
> import numpy as np
>
> size = []
> colstack_times = []
> vstack_times = []
> for n in [3, 10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000]:
>     print(n)
>     a = np.random.random(n)
>     b = np.random.random(n)
>     size.append(n)
>     t = %timeit -o np.column_stack([a, b])
>     colstack_times.append(t.average)
>     t = %timeit -o np.vstack([a, b]).T
>     vstack_times.append(t.average)
>
> import matplotlib.pyplot as plt
>
> plt.loglog(size, colstack_times, "o:", label="column_stack()")
> plt.loglog(size, vstack_times, "o:", label="vstack().T")
> plt.xlabel("array size")
> plt.ylabel("time")
> plt.legend()
> ```
> </details>
>
> the gain is not so clear. It depends on the array size.
>
> <img width="572" height="426" alt="Image" src="https://github.com/user-attachments/assets/450f8ab0-cfba-4c5e-ad2b-8730ca0c2b30" />
>
> Only larger arrays (N>=3000) benefit. While one cound argue that small arrays are fast anyway, I find the result not compelling enough to run through the codebase and change everything.
>
> Context from the numpy issue tracker:
> - https://github.com/numpy/numpy/issues/8082
> - https://github.com/numpy/numpy/issues/10321
> - https://github.com/numpy/numpy/issues/320
> Gist: `np.column_stack` is somewhat slower. Reasons are the ability to accept column blocks (only the first dimension has to match) and the different memory layout, which may or may not make `vstack().T` faster, also depending on the subsequent access patterns.
>
> I also want to note that https://github.com/numpy/numpy/issues/8082#issue-17864496 measured 10 years ago that `column_stack()` was a bit faster than `vstack().T`. So performance characteristics can change over time and I do not think it's worth chasing microsecond performance gains in such a scenario. If we see the need for such mirco-optimization, IMHO we should limit this to hot spots and add performance tests for different implementations so that we note when our "optimized solution" does not perform well anymore.

### Comment 4: anntzer (2026-02-11T09:46:41Z)
> FWIW I observe a smaller gain for column_stack for small arrays, and a switch at a lower value (100-300 elements), but I agree we should test this properly if we make that change.
> <img width="640" height="488" alt="Image" src="https://github.com/user-attachments/assets/cac01e0c-7147-472d-8f39-838b1dd8b79a" />

### Comment 5: scottshambaugh (2026-02-11T10:35:06Z)
> I think I have an older machine than most of you, my results are not as smooth :). I personally find a 30-50% boost at large `n` pretty compelling, but have no issues with closing this and just making changes in the hot paths where we find them.
>
> Putting together a benchmark suite has been on my personal TODO for a while. I'm not sure that it would be useful for catching behavior changes like this however where total impact on runtime from any given call is on the order of a percent or two. That'll get largely washed out in the noise for E2E plotting times, even if more targeted inspections like we are doing here show a difference. Part of why I've been bundling performance improvements - a single change can be hard to justify even if they stack up in the aggregate.
>
> <img width="726" height="552" alt="Image" src="https://github.com/user-attachments/assets/655a72ac-a002-45c9-b25c-55af53ca8e57" />

### Comment 6: timhoffm (2026-02-11T10:43:28Z)
> I'm not surprised that you see different numbers. These micro-performance aspects depend on many variables (Python version, numpy version, CPU architecture (e.g. apple silicon vs x86), CPU features like SIMD instructions, CPU cache size). It's really difficult to get a clear recommendation which one is better.
>
> I therefore believe we should focus on other kinds of performance optimizations like preventing unnecessary or duplicate work or extensive python loops. These improvements are clearer and more persistent.

### Comment 7: scottshambaugh (2026-02-11T10:46:22Z)
> Works for me!

### Comment 8: jklymak (2026-02-11T14:55:30Z)
> Note that we have a benchmark suite.  https://matplotlib.org/mpl-bench/
>
> But it is probably not routinely run, whereas I think it should be run more often to make sure we are not regressing on speed

### Comment 9: Borda (2026-02-12T17:49:12Z)
> After reviewing the linked PRs, please don't touch this issue regardless of the entity; it is a minefield and will likely be closed for whatever bias-related reason... :D

### Comment 10: story645 (2026-02-12T18:11:55Z)
> Per the reasons for the closure of this PR, it's unclear whether there are consistent performance gains from this change; therefore we will not be accepting PRs that target this issue.
> If someone runs a bench marking suite (such as mpl-bench) and shows clear consistent gains such that this issue is worth reopening, let us know about the performance gains on discourse.matplotlib.org.
>
> Comments on our AI policy should be directed to https://discourse.matplotlib.org/t/ai-policy-discussion/26116
