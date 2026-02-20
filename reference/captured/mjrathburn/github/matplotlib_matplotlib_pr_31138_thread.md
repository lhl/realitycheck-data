# matplotlib/matplotlib PR #31138: [PERF] Replace np.column_stack with np.vstack().T (HUMAN EDITION)
- **Source**: https://github.com/matplotlib/matplotlib/pull/31138
- **Retrieved (UTC)**: 2026-02-20T05:57:37Z
- **state**: closed
- **merged**: False
- **created_at**: 2026-02-12T12:51:30Z
- **updated_at**: 2026-02-12T14:34:20Z
- **closed_at**: 2026-02-12T13:24:24Z
- **Participants (unique)**: bergutman, github-actions[bot], gjazeron, IanKemp, JEpifanio90, timhoffm

## Body
> This PR addresses issue [#31130](https://github.com/matplotlib/matplotlib/issues/31130) by replacing specific safe occurrences of `np.column_stack` with `np.vstack().T` for better performance.
>
> **IMPORTANT:** This is a more targeted fix than originally proposed. Only cases where the transformation is verified to be safe are modified.
>
> ### Performance Improvement
>
> According to benchmarks in issue [#31130](https://github.com/matplotlib/matplotlib/issues/31130):
>
> - With broadcast: `np.column_stack` → 36.47 µs, `np.vstack().T` → 27.67 µs (24% faster)
> - Without broadcast: `np.column_stack` → 20.63 µs, `np.vstack().T` → 13.18 µs (36% faster)
>
> The improvement comes from `np.vstack().T` doing contiguous memory copies and returning a view, whereas `np.column_stack` has to interleave elements in memory.
>
> ### Transformation Safety
>
> `column_stack([A, B])` is equivalent to `vstack([A, B]).T` ONLY when:
>
> 1. Both A and B are 1D arrays of the same length
> 2. Both A and B are 2D arrays of the same shape
>
> Cases where arrays have different dimensions (e.g., 2D + 1D) are NOT safe for this transformation.
>
> ### Changes
>
> - Modified 3 files
> - Replaced 3 occurrences of `np.column_stack` with `np.vstack().T`
> - All changes are in production code (not tests)
> - Only verified safe cases are modified
> - No functional changes - this is a pure performance optimization
>
> ### Files Modified
>
> - `lib/matplotlib/lines.py`: Line2D.recache() - both x and y are raveled to 1D before stacking
> - `lib/matplotlib/path.py`: Path.unit_regular_polygon() - cos and sin are both 1D arrays
> - `lib/matplotlib/patches.py`: StepPatch - x and y are both 1D arrays
>
> ### Testing
>
> The changes maintain exact same behavior as before. The existing test suite should pass without modification.
>
> Closes [#31130](https://github.com/matplotlib/matplotlib/issues/31130)

## Comments

### Comment 1: github-actions[bot] (2026-02-12T12:51:41Z)
> Thank you for opening your first PR into Matplotlib!
>
> If you have not heard from us in a week or so, please leave a new comment below and that should bring it to our attention. Most of our reviewers are volunteers and sometimes things fall through the cracks.
>
> You can also join us [on gitter](https://gitter.im/matplotlib/matplotlib) for real-time discussion.
>
> For details on testing, writing docs, and our review process, please see [the developer guide](https://matplotlib.org/devdocs/devel/index.html).
> **Please let us know  if (and how) you use AI, it will help us give you better feedback on your PR.**
>
> We strive to be a welcoming and open project. Please follow our [Code of Conduct](https://github.com/matplotlib/matplotlib/blob/main/CODE_OF_CONDUCT.md).

### Comment 2: bergutman (2026-02-12T12:56:38Z)
> Original PR from #31132 but now with 100% more meat. Do you need me to upload a birth certificate to prove that I'm human?

### Comment 3: gjazeron (2026-02-12T13:06:50Z)
> at least it's entertaining

### Comment 4: IanKemp (2026-02-12T14:00:39Z)
> > Original PR from #31132 but now with 100% more meat. Do you need me to upload a birth certificate to prove that I'm human?
>
> No, the maintainers simply want you to comply with the rules for contributing to this repository - rules that are available via a link in the original issue, and were reinforced by a comment from a maintainer there. Disagreeing with those rules is fine, wanting to change those rules is fine, but there are constructive ways to accomplish that - and you've done the exact opposite. Breaking the rules was bad, insulting one of the maintainers was worse, yet instead of owning these mistakes and learning from the experience, you've compounded them by being unwarrantedly passive-aggressive. Take it from experience - that's not a winning strategy.

### Comment 5: JEpifanio90 (2026-02-12T14:13:59Z)
> > > Original PR from #31132 but now with 100% more meat. Do you need me to upload a birth certificate to prove that I'm human?
> > 
> > No, the maintainers simply want you to comply with the rules for contributing to this repository - rules that are available via a link in the original issue, and were reinforced by a comment from a maintainer there. Disagreeing with those rules is fine, wanting to change those rules is fine, but there are constructive ways to accomplish that - and you've done the exact opposite. Breaking the rules was bad, insulting one of the maintainers was worse, yet instead of owning these mistakes and learning from the experience, you've compounded them by being unwarrantedly passive-aggressive. Take it from experience - that's not a winning strategy.
>
> ~Plus the health checks didn't pass for either PR~. If you're going to stand your ground like that (which, again, wasn't good) at least make sure the code is up to the standard of the codebase...

### Comment 6: IanKemp (2026-02-12T14:22:01Z)
> > > > Original PR from #31132 but now with 100% more meat. Do you need me to upload a birth certificate to prove that I'm human?
> > > 
> > > 
> > > No, the maintainers simply want you to comply with the rules for contributing to this repository - rules that are available via a link in the original issue, and were reinforced by a comment from a maintainer there. Disagreeing with those rules is fine, wanting to change those rules is fine, but there are constructive ways to accomplish that - and you've done the exact opposite. Breaking the rules was bad, insulting one of the maintainers was worse, yet instead of owning these mistakes and learning from the experience, you've compounded them by being unwarrantedly passive-aggressive. Take it from experience - that's not a winning strategy.
> > 
> > Plus the health checks didn't pass for either PR. If you're going to stand your ground like that (which, again, wasn't good) at least make sure the code is up to the standard of the codebase...
>
> The same tests [are currently failing on the main branch](https://github.com/matplotlib/matplotlib/actions/runs/21887956937), so this PR did not break anything there.

### Comment 7: timhoffm (2026-02-12T14:33:41Z)
> Thanks all for discussing and contributing. We have come to the conclusion that the optimization is not worth it. See the discussion in the original issue https://github.com/matplotlib/matplotlib/issues/31130. That closes the topic.
>
> I'll lock the thread, because discussing appropriateness of past behavior does not move the project forward.
