# CHANGELOG



## v1.1.1 (2024-02-09)

### Build

* build: configure `codespell` to fix misspellings

Requires python^3.11.0 to use pyproject.toml

Exclude everything in `docs/_build`,
and the exact lines in `.codespell.ignore`

Also add to pre-commit checks ([`37bac3d`](https://github.com/computational-psychology/stimupy/commit/37bac3d708c8eb11f897ea09dfe94acabe5fdba1))

* build: only trigger publishing workflow once per release ([`44a303b`](https://github.com/computational-psychology/stimupy/commit/44a303bc0c54f052605c0d7922ff21168a30b254))

### Documentation

* docs(periodics): fix Gabor argument `intensities` ([`533e1e2`](https://github.com/computational-psychology/stimupy/commit/533e1e258ac7523eefdaa30ba630c48cec8a722b))

* docs(tutorial): fix references to `two_sided` ([`19f59a9`](https://github.com/computational-psychology/stimupy/commit/19f59a9f90f82485f60cfd68205ddfce0ed254c5))

### Fix

* fix(checkerboards): define multiple target intensities

Previously, checkerboards could only draw a single target intensity, even if multiple targets are specified. For some stimuli however, I want to have two target checks, each with a different intensity value.

Use components.draw_regions to do the actual target drawing. Ensures consistency with other stimuli with targets. ([`ab525b3`](https://github.com/computational-psychology/stimupy/commit/ab525b3cc509b258df1f197026dec00311b77c00))

* fix(checkerboards): define multiple target intensities

Use `components.draw_regions` to do the actual target drawing. Ensures consistency with other stimuli with targets ([`442bd29`](https://github.com/computational-psychology/stimupy/commit/442bd2908667e6e42da979cb3fdbcc09f95c8b34))

* fix(RHS2007): WE_dual separate mask for each target

Previously, the targets in black were lumped together, as were the targets in white. Now, each target, in each of the two stimuli, has its own mask idx ([`0b78372`](https://github.com/computational-psychology/stimupy/commit/0b78372f5c44677bba59dcf4f109f087770b0739))

* fix(whites): enable specifying either 1, or multiple target indices

Some configuration was causing errors ([`ba552b9`](https://github.com/computational-psychology/stimupy/commit/ba552b9c698ff45e0901bee859bd1365c0012ccf))

* fix(text): remove text direction argument

Pillow is complaining about `libraqm` not being installed. Previously, it was not complaining about this. This problem seems to be limited to asking for a writing direction -- without that, Pillow no longer complains ([`6cceca6`](https://github.com/computational-psychology/stimupy/commit/6cceca65fd1c49c5a4f2363c64c3e8e4a277258f))

### Style

* style: use codespell to fix misspellings ([`de8efb4`](https://github.com/computational-psychology/stimupy/commit/de8efb4ece275f025713b69ccaff4e48c38539a6))

### Test

* test(RHS2007): regen ground truth

Only mask of WE_dual changed ([`6c76f2e`](https://github.com/computational-psychology/stimupy/commit/6c76f2e59b0f70644f72fa32e42d62406536bd13))

### Unknown

* Merge pull request #121 from computational-psychology/dev

Bugfixes ([`da97ecf`](https://github.com/computational-psychology/stimupy/commit/da97ecf024fb7b477181412715faf2d5779d4d77))

* Merge branch `main` into dev ([`1d4371a`](https://github.com/computational-psychology/stimupy/commit/1d4371adf53aa6d6cf4eed49978b26158bd9d7bc))

* Merge pull request #120 from computational-psychology/build

Update build-system ([`d56e528`](https://github.com/computational-psychology/stimupy/commit/d56e528a16bc52f39c6d48099c892157932353a2))

* Merge pull request #118 from computational-psychology/fix/whites_targets

fix(whites): enable specifying either 1, or multiple target indices ([`8ec7d6e`](https://github.com/computational-psychology/stimupy/commit/8ec7d6e801c7c97846f6895e7060fe0f20d17459))

* Merge pull request #117 from computational-psychology/fix/RHS2007

Fix(RHS2007): Individually mask each target in WE_Dual ([`3cba67d`](https://github.com/computational-psychology/stimupy/commit/3cba67ddc5c66a2007de41317807b6bcc2c76d5a))

* Merge pull request #119 from computational-psychology/fix/text

fix(text): remove text direction argument ([`759f8e8`](https://github.com/computational-psychology/stimupy/commit/759f8e82da6c79874b7d82e36144850b3b985c13))


## v1.1.0 (2023-09-21)

### Build

* build: update PSR config ([`8659604`](https://github.com/computational-psychology/stimupy/commit/8659604816c0a816d8631c41530fbb06d47c46d8))

* build: update versioning to use python-semantic-release@v8.0 ([`e0cd11e`](https://github.com/computational-psychology/stimupy/commit/e0cd11e9d955afc01d8fbd21a7a161ce0d776e91))

* build(manuscript): allow manual trigger ([`b46fdf8`](https://github.com/computational-psychology/stimupy/commit/b46fdf835259c6689dcbb4f442dc230c354cc38a))

### Chore

* chore: autoformat ([`106dee7`](https://github.com/computational-psychology/stimupy/commit/106dee79d0eab24248cde1bcf1c4cf83bc3a0ffb))

* chore: autoformat ([`95ccba7`](https://github.com/computational-psychology/stimupy/commit/95ccba7af67cd424d095c0e6d18055c02d4a4b08))

* chore(autoformat): update pre-commit config ([`47c408c`](https://github.com/computational-psychology/stimupy/commit/47c408c6e23a8f3affca18eb7f6016b833d4ebd4))

* chore: (auto)format ([`dea6b57`](https://github.com/computational-psychology/stimupy/commit/dea6b57cad00d9abc6b3cce11ba9a9607f944cb7))

### Documentation

* docs(demos): `sbcs.generalized_two_sided()` demo ([`7318280`](https://github.com/computational-psychology/stimupy/commit/7318280699e0390c9f6fdf1181fa7376e11c2e42))

* docs(demos): `sbcs.square_two_sided`, `.circular_two_sided` demos ([`e781cfb`](https://github.com/computational-psychology/stimupy/commit/e781cfbe5652acf0d9dbfcf13ac61641b3ed6b97))

* docs(sbcs): unify docstrings ([`60d3c80`](https://github.com/computational-psychology/stimupy/commit/60d3c808c0fb846209a5dd0d7dd9d8ed97711694))

* docs(frames): docstrings ([`5d83551`](https://github.com/computational-psychology/stimupy/commit/5d8355136bfdf64770d0199aa986dda15b059cd3))

* docs(radials): docstrings ([`fd79e0b`](https://github.com/computational-psychology/stimupy/commit/fd79e0bc7cf64e90cc251cc956d39564ea2b5773))

* docs(demos): update `two_sided` demos ([`c2beace`](https://github.com/computational-psychology/stimupy/commit/c2beace115377b571bf247086b7db2c56053f781))

* docs(demos): bullseyes.circular_generalized ([`25669ca`](https://github.com/computational-psychology/stimupy/commit/25669ca4966525cb9c2c5e6556e6d19aeac39670))

* docs(demos): rings.circular_generalized ([`a19a1c4`](https://github.com/computational-psychology/stimupy/commit/a19a1c45e4e40f78a40528f1ffd1386e3f483f88))

* docs(demos): fix White's demo ([`37b70c3`](https://github.com/computational-psychology/stimupy/commit/37b70c327a360aa1d94655b8e786e80eac429f50))

* docs(demos): text demo ([`ef686f3`](https://github.com/computational-psychology/stimupy/commit/ef686f3e8ae280905938538d8479127475c3e16d))

* docs(demos): add support for two-sided parameter specification ([`aec4043`](https://github.com/computational-psychology/stimupy/commit/aec4043280ffbc42b0c8ef353669d15cad89033e))

* docs(citation): add to TOC ([`c2a9574`](https://github.com/computational-psychology/stimupy/commit/c2a95748674db1333d66abc10bc2d4b9238a897f))

* docs(citation): reformat ([`e940428`](https://github.com/computational-psychology/stimupy/commit/e940428dc659c41cd79b5fc9403b765bdd3e3fe4))

* docs: added citation to readme and docs ([`6279322`](https://github.com/computational-psychology/stimupy/commit/6279322a7bded7bbc30bd724e29d177edc67e328))

* docs(manuscript): &#34;use case&#34; as two words ([`c3d999c`](https://github.com/computational-psychology/stimupy/commit/c3d999c1d689e29981cb1d010444d9dd6ed28d4b))

* docs: final touchup on manuscript ([`d3c04ef`](https://github.com/computational-psychology/stimupy/commit/d3c04ef7729071ac2bed998782d17bcc4c375225))

* docs(manuscript): update references ([`f57ec56`](https://github.com/computational-psychology/stimupy/commit/f57ec5658df6c821782cd1c869eef744d9eec206))

* docs: final touch-up on manuscript ([`2f37a9d`](https://github.com/computational-psychology/stimupy/commit/2f37a9da4236172d0dd156084ca6308143c58ead))

* docs: changed manuscript title ([`18d95fb`](https://github.com/computational-psychology/stimupy/commit/18d95fba62353bb4fdefe0023a86be082c92ff6f))

* docs: made editorial changes to manuscript ([`856c8a9`](https://github.com/computational-psychology/stimupy/commit/856c8a9f9441381c567dba67d82d70215ea6621c))

### Feature

* feat(sbcs): `sbcs.generalized_two_sided()` ([`dbfbab1`](https://github.com/computational-psychology/stimupy/commit/dbfbab154a5dd875a5e5633835643c4fbec993b3))

* feat(sbcs.gen): enable rotation in generlized SBC

Closes #39 ([`bfe946b`](https://github.com/computational-psychology/stimupy/commit/bfe946bf516517d5a3a8fe9489a37ed12fe82c2e))

* feat(sbcs): `_two_sided` versions of all `sbcs.` ([`7bac6a1`](https://github.com/computational-psychology/stimupy/commit/7bac6a1ed0129a39e451d89656932d9e152ef5c0))

* feat(sbcs): `sbcs.circular`, `.square`

Pass-through wrappers based off `bullseyes.&lt;&gt;` ([`0ff0213`](https://github.com/computational-psychology/stimupy/commit/0ff0213ad4d5a162409ede6fccf9cf2ade02e047))

* feat(two-sided): utility wrapper-function to create two-sided stimuli ([`624bf50`](https://github.com/computational-psychology/stimupy/commit/624bf500c60fdb35e9cd30cd9a7b00f96e43462d))

* feat(stimuli): bullseyes.circular_generalized ([`8b9ad10`](https://github.com/computational-psychology/stimupy/commit/8b9ad109ea311b60efef7767f29a5731f0aa4d41))

* feat(stimuli): rings.circular_generalized ([`7e0cf7c`](https://github.com/computational-psychology/stimupy/commit/7e0cf7c321a81827e826760bb2f17a75963abc8f))

* feat: components.texts ([`88d5ffc`](https://github.com/computational-psychology/stimupy/commit/88d5ffc58762f562285e001db784f45af7a23668))

### Fix

* fix(disk): mask is now properly aligned

Fix by basing `disk` on `rings` rather than on `ring` ([`911cbd6`](https://github.com/computational-psychology/stimupy/commit/911cbd6c679840850a6c7910463c297555bcf0df))

* fix: rename `_mask`s

Add a distance-specific mask (`bar_`, `ring_`, `frame_`, `segment_`). These are similarly named in the &#34;generalized&#34; versions of these stimuli (`frames`, `rings`, etc.).
This is just a reference to `grating_mask`, so that will remain consistent between all `wave`-like stimuli.

Closes #102 ([`2cc9222`](https://github.com/computational-psychology/stimupy/commit/2cc9222231be9b9519e99dd0773eb521af65aa39))

* fix(bullseyes): update bullseye target specification

Now that indexing is 1-based. ([`92c9e1b`](https://github.com/computational-psychology/stimupy/commit/92c9e1bff2fd92771db0ea025c3cc26d8ddd733f))

* fix(pad_dict): should also update ppd, visual_size, if it can ([`dab5bf5`](https://github.com/computational-psychology/stimupy/commit/dab5bf5e93dc2ed6133b79e4ef69a50b4e43b5c5))

* fix(RHS2007): correct targets in Todorovic' Benary 1_2, 3_4

Closes #90

1_2_3_4() was already correct.
Others now use that one as base ([`520c659`](https://github.com/computational-psychology/stimupy/commit/520c6590c3239cc6a45f4423cf8f2b39fd8fe7e3))

### Refactor

* refactor(papers): use `sbcs.&lt;&gt;_two_sided()` in papers

`domijan2015.simultaneous_brightness_contrast()`
`RHS2007.sbc_small()`
`RHS2007.sbc_large()` ([`3ee13ed`](https://github.com/computational-psychology/stimupy/commit/3ee13edeb2258e1384a8d8763792c519d6fb0d6b))

* refactor(radials): more integrated drawing ([`afcdc3e`](https://github.com/computational-psychology/stimupy/commit/afcdc3e731dc6af32e293c655f3fd9479d3aeb96))

* refactor(gratings,papers): update intensities order ([`1ab048a`](https://github.com/computational-psychology/stimupy/commit/1ab048a4a4fc78d927041f4169f1154259709bb5))

* refactor: unify `intensity_` arguments

(almost) all `(0.0, 1.0)`

Closes #80 ([`a00295f`](https://github.com/computational-psychology/stimupy/commit/a00295f5cf9fc54cbea892b6674c1e682114b809))

* refactor(waves): pass intensities through

Addresses #80 ([`44d7f79`](https://github.com/computational-psychology/stimupy/commit/44d7f79be71d146f35cde145b080bd918b41c594))

* refactor(modelfest): more explicit conversions ([`be4b53d`](https://github.com/computational-psychology/stimupy/commit/be4b53df2f59d2acba3cd9e95245f6408b3b7fb5))

* refactor(stimuli): use two-sided utility wrapper ([`8ac1717`](https://github.com/computational-psychology/stimupy/commit/8ac1717b791a5d7f46b29c5913f8dd96cbfc6881))

* refactor(papers): update to use 1-based indexing of elements in Whites ([`e1c3101`](https://github.com/computational-psychology/stimupy/commit/e1c310172af615ca663bf343b1d7f6a15f4f11e2))

* refactor(papers): update to use 1-based indexing of elements ([`bd90b8e`](https://github.com/computational-psychology/stimupy/commit/bd90b8e0968381855c4dc889adbe5d7d4e4c078f))

* refactor(whites): use `mask_targets()` ([`1e04f07`](https://github.com/computational-psychology/stimupy/commit/1e04f0756212ecc718bb93942006bcdf69e81ff2))

* refactor(waves): integrate `place_targets()` ([`daf6acd`](https://github.com/computational-psychology/stimupy/commit/daf6acd63b7b1cb80d38f24932d7c63d7934c533))

* refactor: target_indices defaults to (), but can handle None

Closes #97 #98 ([`9e8d136`](https://github.com/computational-psychology/stimupy/commit/9e8d13622ad616b0df332a56688da91eccd5f0ea))

* refactor(rings): use `place_targets()` in `rings_generalized()` ([`2da1b65`](https://github.com/computational-psychology/stimupy/commit/2da1b6538ddcd711d3be726e1aabf3a3b893f6c5))

* refactor(pinwheels): integrate `mask_targets()` ([`c748706`](https://github.com/computational-psychology/stimupy/commit/c748706e2d5d1a2a7c64400dbf2ba138c2a2da85))

* refactor(stimuli): `place_targets()`

actually places targets in stimulus-dict ([`fff6f14`](https://github.com/computational-psychology/stimupy/commit/fff6f14d97ae26c063bbb3720ec65b5905529a22))

* refactor(stimuli): `mask_targets()`

to standardize logic of indicating elements of gratings etc. as targets, which is a big par of the `stimuli`
Also allows for negative element indices, counting backwards from the highest element index

Closes #12 ([`9232891`](https://github.com/computational-psychology/stimupy/commit/92328911e6240d5ba7916be6e918d4311705e5c4))

* refactor(export): guard clauses, pathlib ([`e59fc51`](https://github.com/computational-psychology/stimupy/commit/e59fc51c49d1f1db0b3627d02d4c67d3c89c5ac0))

### Style

* style: autoformat pyproject.toml ([`b153d5e`](https://github.com/computational-psychology/stimupy/commit/b153d5e5cb8d5a0a04481e0ff0e0829b143f2bdf))

* style: autoformat ([`962a332`](https://github.com/computational-psychology/stimupy/commit/962a332f598922f13012207798f2c189ebc9d5b6))

### Test

* test: update ground truth

single pixel changes in RHS2007_WE_radial_* ([`f4e4d48`](https://github.com/computational-psychology/stimupy/commit/f4e4d480b562318ef25f824caa2cc4b251dcc875))

* test(modelfest): update `Disk40()`and its groundtruth

Slightly decrease radius. This is actually results in an image that is exactly identical as the original published `disk40.tif` image (unlike previous ground truth, which was 4pix off) ([`30c9738`](https://github.com/computational-psychology/stimupy/commit/30c9738d1f7305d30b02840ba5233478ecac92e7))

* test(modelfest): isolate code to test correspondence to original images ([`4c44c88`](https://github.com/computational-psychology/stimupy/commit/4c44c881319d9611008ca3b2d508465877e657fd))

* test: extract function for image comparison ([`813e3a2`](https://github.com/computational-psychology/stimupy/commit/813e3a24b478a8999e0cf1ce211cf086bab4126f))

* test: fix gen_ground_truth ([`5ad8cb3`](https://github.com/computational-psychology/stimupy/commit/5ad8cb31cb31eacbc7a8e2e1c176f7d9d6b9160f))

### Unknown

* Merge pull request #114 from computational-psychology/build_psr

Build: update python-semantic-release configuration ([`e281e9a`](https://github.com/computational-psychology/stimupy/commit/e281e9a2d0a00f836e302577f5e258c996d6e25e))

* Merge pull request #108 from computational-psychology/dev

New features, refactoring, and fixes ([`3788170`](https://github.com/computational-psychology/stimupy/commit/37881707d5e38069a951d092012d249f9952cab7))

* Merge pull request #107 from computational-psychology/feat_sbcs_circular

Add more `sbcs.`.
`sbcs.square()` and `sbcs.circular()`, parameterized using `target_radius` and `surround_radius`, based on `bullseyes.square()` and `.circular()`. 
Adds some `_two_sided()` versions as well, which are now used in some `papers`.
Also enable `rotation` arg in `sbcs.generalized()`. ([`d1510e9`](https://github.com/computational-psychology/stimupy/commit/d1510e9b45f629b8c4fa9fc64a8512016dd83780))

* docs(demos):`sbcs.circular`, `.square` demos ([`81b5528`](https://github.com/computational-psychology/stimupy/commit/81b552898c664522e0f6a28840822d12a17351ac))

* Merge pull request #106 from computational-psychology/refactor_two_sided

Easier `_two_sided`-stimuli functions ([`7ba0bee`](https://github.com/computational-psychology/stimupy/commit/7ba0beeb618b82a3c9963dd1dc3cd308bd98f753))

* Merge branch `dev` into refactor_two_sided ([`db94838`](https://github.com/computational-psychology/stimupy/commit/db9483882c7265236045fd3a9e81fa0dec1ad788))

* Merge pull request #103 from computational-psychology/refactor_intensities

Unify `intensity_`arguments ([`4ff38d5`](https://github.com/computational-psychology/stimupy/commit/4ff38d5d26632959e231ef6fce445fc0d14ea5c4))

* Merge pull request #104 from computational-psychology/test_modelfest

Refactor ModelFest comparison to original images ([`4218dc3`](https://github.com/computational-psychology/stimupy/commit/4218dc3d41104fe40c0a69005b32141368d9b4e5))

* Merge pull request #101 from computational-psychology/refactor_targets

Refactor target placement in various stimuli.

Add `mask_targets()` and `place_targets()` general-purpose functions which can be used to designate target &#34;elements&#34; (bars, rings, frames, etc.) from an existing `_mask`.

Integrate new functions into `waves`, `pinwheels`, `rings` and `whites`

Add `rings.circular_generalized()` and `bullseye.circular_generalized()` using new functions

This single-implementation of target placement has the advantage that it all works the same: first element is 1, target_indices can be negative (counting &#34;backwards&#34; from the last bar/ring/etc.). ([`885ec6c`](https://github.com/computational-psychology/stimupy/commit/885ec6c59af9fc1fcf9cf92333581e433746574f))

* Merge pull request #100 from computational-psychology/build_refresh

build: update versioning to use python-semantic-release@v8.0 ([`16a3496`](https://github.com/computational-psychology/stimupy/commit/16a34966c5c1de624319943ca17b5f205ac9b4dc))

* Merge pull request #96 from computational-psychology/fix_twosided_params

fix: two-sided params for `_two_sided`-stimuli ([`1188af5`](https://github.com/computational-psychology/stimupy/commit/1188af55f2476e516b7d675a2e07b16ee780fdce))

* Merge pull request #95 from computational-psychology/feat_text

feat: text ([`e0effc0`](https://github.com/computational-psychology/stimupy/commit/e0effc0135651af09d5b010d1ececd038bc74b73))

* Merge pull request #94 from computational-psychology/fix_RHS2007_TodorovicBenary

fix(RHS2007): correct targets in `todorovic_benary_1_2()`, `3_4()` ([`00af7d2`](https://github.com/computational-psychology/stimupy/commit/00af7d2494b230b4cd57db46e4d936a907773b2a))

* use default ImageFont ([`bc56a41`](https://github.com/computational-psychology/stimupy/commit/bc56a41be7b378d13b6dfce9860c2763de7cbd9a))

* Todorovics ([`a010d4a`](https://github.com/computational-psychology/stimupy/commit/a010d4aa5a3755a9e48132bdf0aa54f48996f983))

* SBCs

Closes #92 ([`5569a12`](https://github.com/computational-psychology/stimupy/commit/5569a1261314af892d2600bf8e9b741d361319bd))

* Rings &amp; Bullseyes ([`23fc041`](https://github.com/computational-psychology/stimupy/commit/23fc04142d72f4bea8fd5856dedbeaf341046ce7))

* Mueller-Lyer ([`6b01cce`](https://github.com/computational-psychology/stimupy/commit/6b01cce10442a756c9d0034b386c8c27c0f01352))

* DelBoueufs ([`587aed5`](https://github.com/computational-psychology/stimupy/commit/587aed5d7b85ffa986fe89b245ad9f77bf08383e))

* Update tests ([`fbd1dc4`](https://github.com/computational-psychology/stimupy/commit/fbd1dc470f6e61d09d868d7b8ee68143c0d8fe36))

* Merge pull request #91 from computational-psychology/dev_citation

docs: added citation to readme and docs ([`316ded8`](https://github.com/computational-psychology/stimupy/commit/316ded807c782fbf1eab404ca0490d3a62b03f1e))

* Merge pull request #89 from computational-psychology/dev_manuscript

docs: final touchup on manuscript ([`ca8bf43`](https://github.com/computational-psychology/stimupy/commit/ca8bf4350c39cae79c66285c4243863fc5c1055f))

* Merge pull request #88 from computational-psychology/dev_manuscript

docs: final touch-up on manuscript ([`f756c54`](https://github.com/computational-psychology/stimupy/commit/f756c540fba885ffaa27cd92fde96e601193c004))

* Merge pull request #87 from computational-psychology/dev_manuscript

Final editorial (&amp; title) changes to manuscript ([`b4bb148`](https://github.com/computational-psychology/stimupy/commit/b4bb1484ab26b6689bacc40d6e60fd01eb2d1cec))


## v1.0.0 (2023-05-23)

### Breaking

* build: public release, unpin major version

BREAKING CHANGE: bump to v1.0.0 ([`4ac4aee`](https://github.com/computational-psychology/stimupy/commit/4ac4aee80bb9529bd28c8c5be05d3d725572feea))

### Build

* build(release): publish to PyPI (&amp; testPyPI), using trusted publisher

Having specified a &#34;trusted publisher&#34; (the repository and GHA workflow), no tokens and secrets are necessary.

BREAKING: Bump to v1.0.0 ([`51b0d0e`](https://github.com/computational-psychology/stimupy/commit/51b0d0eff997d0c78eeb34b69af4369fb4ecbe4f))

### Chore

* chore: autoformat ([`bd2a9bb`](https://github.com/computational-psychology/stimupy/commit/bd2a9bb51066968cfc8b284702746cfeec4b72f7))

### Documentation

* docs(README): add badges ([`e8f54f9`](https://github.com/computational-psychology/stimupy/commit/e8f54f9ab4c4772e3433388caa7c62506efc883a))

* docs: update installation instructions to use PyPI ([`4c3c492`](https://github.com/computational-psychology/stimupy/commit/4c3c49227dadabb7ef1950702f0e05079982f2d1))

### Fix

* fix: build GHA ([`db12dda`](https://github.com/computational-psychology/stimupy/commit/db12dda349df0ce2e98b0f715d04aed242d3d9dd))

### Unknown

* v1.0.0

Automatically generated by python-semantic-release ([`5461a7c`](https://github.com/computational-psychology/stimupy/commit/5461a7c956501c2755732b6f13e2213874f9f4e4))

* Merge: Release to PyPI as v1.0.0

Enable automated release, bump to v1.0.0.
Also update installation instructions. ([`0bad0bd`](https://github.com/computational-psychology/stimupy/commit/0bad0bdfa0892ed4bd714cecbdae9e434e41dd66))

* fix (whites): if no index is provided, does not require target_heights anymore ([`6bd55ae`](https://github.com/computational-psychology/stimupy/commit/6bd55ae9c3c4eaa7c8fa1b7fbf08c8452e09f7c7))


## v0.101.1 (2023-05-20)

### Build

* build: fix regex for release GHA ([`fc19d2a`](https://github.com/computational-psychology/stimupy/commit/fc19d2a0b9363a72198e4f74df72e3284df68149))

### Documentation

* docs(manuscript): add comparison to OCTA ([`551f80d`](https://github.com/computational-psychology/stimupy/commit/551f80d8bde4aa217d7a52a8c1e07cbe9adaef08))

* docs: added missing arg-information to logo-function ([`73e5a27`](https://github.com/computational-psychology/stimupy/commit/73e5a2750d96772fe47add14a97a3a2803f25c07))

* docs: minor fix landing page ([`fc8deb4`](https://github.com/computational-psychology/stimupy/commit/fc8deb4dee9c1fc09c7495691feb49beb38225f0))

* docs: add logo ([`1fce581`](https://github.com/computational-psychology/stimupy/commit/1fce58114fe5888f0c3381b16e49f771684e49b7))

### Fix

* fix: added relevant error message in todorovic ([`0cb7f88`](https://github.com/computational-psychology/stimupy/commit/0cb7f88a75d78e5ae8d94df3c7363c899b0baaa6))

* fix: aligned functions args and output_dictionary keys for stimuli-gratings ([`fba7785`](https://github.com/computational-psychology/stimupy/commit/fba77855e4bcea8a6f766c2198e4f4e06ad5b39d))

* fix: aligned function args and output_dict keys ([`6981318`](https://github.com/computational-psychology/stimupy/commit/6981318e76f1d9bb594aa94a50b07f4639efe804))

### Style

* style: autoformatting ([`2025e36`](https://github.com/computational-psychology/stimupy/commit/2025e363b06d7ff5d89bafa57ecd10b345f0136b))

### Unknown

* v0.101.1

Automatically generated by python-semantic-release ([`862a64f`](https://github.com/computational-psychology/stimupy/commit/862a64f59b64d4cd2f2cfc717e61f94e5e7f8a9e))

* Merge pull request #84 from computational-psychology/dev_docs

Quality improvements ([`69e0c47`](https://github.com/computational-psychology/stimupy/commit/69e0c479f413cb74b1727e02ad2740ca30fee40a))

* Merge pull request #83 from computational-psychology/dev_docs

docs: very minor fixes ([`e054d55`](https://github.com/computational-psychology/stimupy/commit/e054d55d0d6c2ba045b27a62a46454b2c65e02b3))


## v0.101.0 (2023-05-15)

### Build

* build: fix TestPyPI release GHA ([`108ac44`](https://github.com/computational-psychology/stimupy/commit/108ac4484e04070538c3d7c33fa4022e81e8107b))

### Chore

* chore: format utils.export ([`85e8d83`](https://github.com/computational-psychology/stimupy/commit/85e8d836ad36beda926df47dabb6db7c43c18343))

* chore: autoformat ([`93f6dda`](https://github.com/computational-psychology/stimupy/commit/93f6dda4b7571f0f77f37e29d1a1e76c1b25748f))

### Documentation

* docs: add logo to README ([`4dfabb0`](https://github.com/computational-psychology/stimupy/commit/4dfabb0719ea32c41425e8d8b2cc1f95097b9094))

* docs: typos ([`ce4683d`](https://github.com/computational-psychology/stimupy/commit/ce4683d3f40f0a54530874ad423b5d7140443f75))

* docs: fixed incorrect link in README ([`c2e6575`](https://github.com/computational-psychology/stimupy/commit/c2e65751a79d6b1b13790a49ac7bf700ffa2e6dc))

* docs: updated documentation - mostly language ([`d8f4211`](https://github.com/computational-psychology/stimupy/commit/d8f4211e108f1161fda3cb2c43450caa5822d786))

* docs(guide): axes, orientations, distance_metrics ([`7bc02ec`](https://github.com/computational-psychology/stimupy/commit/7bc02ecb7fac8bfd398ff9fe2e91542a534c172e))

* docs(guides): waves &amp; gratings ([`4d5b507`](https://github.com/computational-psychology/stimupy/commit/4d5b5077ba2203035f201a7947258d7b81a1cc3a))

* docs(howto): sharing

Closes #78 ([`4c950d2`](https://github.com/computational-psychology/stimupy/commit/4c950d2e7feb6cb5ae015f79aa1e2ec8a25e3caa))

* docs(contribute): instructions and examples for contributing paper set ([`17ff040`](https://github.com/computational-psychology/stimupy/commit/17ff040428b7310911fea83ab31d505e7dfa4e94))

* docs(contribute): split up contributing guide into subfiles ([`2cc2cb0`](https://github.com/computational-psychology/stimupy/commit/2cc2cb01cce22f9c753773460e56510c269c0a2c))

* docs(howto): display stimuli (in experiment)

Closes #79 ([`a733b07`](https://github.com/computational-psychology/stimupy/commit/a733b078e4cd057d29435f26d7bb095f887dd4c5))

* docs(howto): export ([`e647773`](https://github.com/computational-psychology/stimupy/commit/e64777398f2f6c51c9e8318a701355a15c8ea2e3))

* docs(howtos): start how-tos ([`8cd970a`](https://github.com/computational-psychology/stimupy/commit/8cd970a645e1ec0a0242b7cc1b3c2457d7ea6745))

* docs(guides): resolution ([`ace6493`](https://github.com/computational-psychology/stimupy/commit/ace64939b5b647665f7694889bee28df5e6b72d4))

* docs: hover_xref configuration for objects ([`c28b7be`](https://github.com/computational-psychology/stimupy/commit/c28b7be15a9903fc49d6e413a5d274e64aabb157))

* docs(demos): better exception-handling, hiding stacktrace

Closes #74 ([`ae98e04`](https://github.com/computational-psychology/stimupy/commit/ae98e04b99b5ffb509935cd67a1fb23a6c659bf2))

* docs(demos): make dependencies explicit

add admonition about dependencies for local running ([`c3b0a0e`](https://github.com/computational-psychology/stimupy/commit/c3b0a0e6e7cf6002c6df83eaa044dd98175877c5))

* docs(readme): fix some typos ([`6983f90`](https://github.com/computational-psychology/stimupy/commit/6983f90426b5dd4ddd162ede42016a70ffdd1b7b))

### Feature

* feat: qr-code with logo embedded ([`a14648e`](https://github.com/computational-psychology/stimupy/commit/a14648eb05f8469e9780aedf2db6d90f3c551722))

* feat: added stimupy logo module, and function ([`0b5b028`](https://github.com/computational-psychology/stimupy/commit/0b5b0281fc444d8a58fce37c9144ce2a882e3f34))

* feat(export): to image, npy, mat, pickle, json ([`3c09c5a`](https://github.com/computational-psychology/stimupy/commit/3c09c5a39f4fabed91f67096df22f8bb920a8002))

* feat: util to create stimspace ([`1679eb5`](https://github.com/computational-psychology/stimupy/commit/1679eb5def54a97f826c3cb7cbbc1a982f194f18))

### Fix

* fix: line_width in ellipse ([`10b7745`](https://github.com/computational-psychology/stimupy/commit/10b77458186e331c721ee3a1d488ab3d32251688))

* fix: added missing demo scripts for edges ([`4c30a3b`](https://github.com/computational-psychology/stimupy/commit/4c30a3bc4a8d2648e9c4bb2e3ab9055916c82762))

* fix: corrected n_cells in dungeon-resolving ([`cd0fc0c`](https://github.com/computational-psychology/stimupy/commit/cd0fc0ca09a85bb829ca23bfe72171c05c66d6db))

* fix: aligned functions args and keys in outputs dicts ([`107edb4`](https://github.com/computational-psychology/stimupy/commit/107edb40a5030274b10de4a962b19939d26818ab))

* fix: aligned functions args and keys in output dicts ([`a3941e7`](https://github.com/computational-psychology/stimupy/commit/a3941e76c43554df8049215ecf439392bc11df1c))

* fix: aligned function-args and keys in output dicts ([`8ab889a`](https://github.com/computational-psychology/stimupy/commit/8ab889a30a933f4f915f9670250265b5977bacca))

* fix: radial and rectilinear waves now correctly  resolve n_phases ([`ecce0b9`](https://github.com/computational-psychology/stimupy/commit/ecce0b9c057ea4eda7d9fc4e3c3ea9b2dff0d008))

* fix(mondrians): clearer error when neither nrows, ncols, depths or intensities are specified ([`f9a5a4d`](https://github.com/computational-psychology/stimupy/commit/f9a5a4d04048040bab367c2b6bdd62307977f657))

* fix: bug in calculating plot-extent from stim-keys ([`240a34a`](https://github.com/computational-psychology/stimupy/commit/240a34a66fa733295bfbc62a154b15a434e9728e))

### Refactor

* refactor(export): consistent naming of exporting funcs

and rename `arr_to_checksum` ([`bbab735`](https://github.com/computational-psychology/stimupy/commit/bbab735e86350a63a93b86f7a6f55bf0b6b29e4e))

* refactor: separate params-permutation and stimspace-stim-creation ([`ae20b4d`](https://github.com/computational-psychology/stimupy/commit/ae20b4d35325b65f559abb44577162f494092ffe))

* refactor: add util modules to init ([`35aae7e`](https://github.com/computational-psychology/stimupy/commit/35aae7e16aad9650557080954dc0746b47aaa89f))

* refactor: add more defaults to `gabor` ([`935673c`](https://github.com/computational-psychology/stimupy/commit/935673cb9f6c1795db62cd3525a9844384ee3df9))

* refactor: edges as `stimuli`-submodule ([`d602fc0`](https://github.com/computational-psychology/stimupy/commit/d602fc05cc7ff6e161b28c278c77880c608289fc))

### Style

* style: autoformat ([`d23efbd`](https://github.com/computational-psychology/stimupy/commit/d23efbdd9a37875a3f7d6bff9220828c123661eb))

* style: autoformatting ([`97238d1`](https://github.com/computational-psychology/stimupy/commit/97238d1704397aeb8f56d3b29a09470fb128c0dc))

* style: auto-formatting ([`fd9e60f`](https://github.com/computational-psychology/stimupy/commit/fd9e60fd1d77dd7b34ba30a48d40a1535d0488ee))

* style: auto-reformatting ([`44c17bf`](https://github.com/computational-psychology/stimupy/commit/44c17bf9d9ea5057feb322341ad2ff0947b14a63))

### Unknown

* v0.101.0

Automatically generated by python-semantic-release ([`c394202`](https://github.com/computational-psychology/stimupy/commit/c3942027cc9f4a2816d64d38f967216fb90bdf98))

* Merge pull request #82 from computational-psychology/dev_docs

Review issues: documentation, exporting, bugfixes. ([`031189a`](https://github.com/computational-psychology/stimupy/commit/031189abc6d618adbbf75e367705fd46a2be1841))

* Merge branch `dev_docs` of https://github.com/computational-psychology/stimupy into dev_docs ([`d16e88f`](https://github.com/computational-psychology/stimupy/commit/d16e88fa5ad8e0b05109e6d3fb5c26d63bdac5ac))


## v0.100.0 (2023-04-10)

### Build

* build: GHA workflow upload release assets to TestPyPI

Downloads assets (sdist, wheel), from latest release-tag, and uploads to PyPI ([`dd37065`](https://github.com/computational-psychology/stimupy/commit/dd37065bd5ef9b7fb83b9edccb187f11ef5c1161))

* build: Provide push permissions through PAT ([`3a54808`](https://github.com/computational-psychology/stimupy/commit/3a54808afde6cd532567f578686049760e7d2018))

* build: Versioning workflow also builds and uploads assets to release-tag

And allow manual trigger ([`927f029`](https://github.com/computational-psychology/stimupy/commit/927f029977707dfce4d5aa237bdd26e5f7f90b18))

* build: specify build system

Use Setuptools build-backend.
Tell PSR to build from `main`, using PyPAs Build ([`649b078`](https://github.com/computational-psychology/stimupy/commit/649b078e087eb14343d10b4b8ea7cc35434c4a68))

* build(version): don't auto-bump to `v1.0.0`

All BREAKING CHANGES will bump minor instead of major version ([`8889e56`](https://github.com/computational-psychology/stimupy/commit/8889e56cbdda3227392729f97267f53656071f7a))

* build: also push version tag ([`a71da54`](https://github.com/computational-psychology/stimupy/commit/a71da5441923bd9a906016b62692a963a9919737))

* build: derive version from commit (not tag)

Because commits will be (more) unambiguous, and if multiple branches have different version-commits, that will need to be resolved in merge-conflicts anyway, thus providing a good check. The alternative, derive from tags, is more fragile: the same commit could have multiple version tags... ([`c2ab046`](https://github.com/computational-psychology/stimupy/commit/c2ab04635b2e93131ee9e0f2f678b66684ba59dd))

* build: only bump on PR merge

and on manual trigger ([`85852e0`](https://github.com/computational-psychology/stimupy/commit/85852e0e3cf3ce4f34216268e11270b8b59414d9))

* build: GHA workflow for bumping version ([`3fc3606`](https://github.com/computational-psychology/stimupy/commit/3fc360653db2a67e4db61fa1520944a8b3eae310))

* build: Create bump-commit as well

Otherwise the updated version numbers in pyproject.toml and __init__.py won't actually be committed ([`c084f69`](https://github.com/computational-psychology/stimupy/commit/c084f6908adc5acfa628f10458b5177434b87cde))

* build: Use PSR to manage version number ([`a1d5e18`](https://github.com/computational-psychology/stimupy/commit/a1d5e18f65f5be2ec93f747234b142399816f8fb))

### Chore

* chore: delete test bump ([`9a9d6eb`](https://github.com/computational-psychology/stimupy/commit/9a9d6eb4bd75526b7f493d93e2817b26e0852bb9))

### Documentation

* docs: Outline dependencies for demos in installation instructions ([`f6a3d98`](https://github.com/computational-psychology/stimupy/commit/f6a3d981d9e43c5567dd6237230819fc60b60403))

* docs(topic guides): hide guides that are under construction ([`8a1146f`](https://github.com/computational-psychology/stimupy/commit/8a1146fb7968227b9add217fa0b54b2e63ccfd3c))

* docs: cleanup installation instructions

Closes #71, Closes #73 ([`3d49f53`](https://github.com/computational-psychology/stimupy/commit/3d49f53d7fbcb8018ce5811f1a0ab67bae75c132))

* docs: update references in replication tutorial ([`2325ce3`](https://github.com/computational-psychology/stimupy/commit/2325ce37b86e8641379ba4e8412ca45251de3033))

* docs(tutorial): more structured overview of `stimuli`

Closes #69 ([`722a977`](https://github.com/computational-psychology/stimupy/commit/722a97799997d091f3445c7e7b8a71446a7bfb45))

* docs: better referencing, using hoverxref ([`5a41f0f`](https://github.com/computational-psychology/stimupy/commit/5a41f0f7e24aab0349f97faca5fed3c925997adc))

* docs(tutorial): more detail on composition, masks

Closes #70 ([`9be4db0`](https://github.com/computational-psychology/stimupy/commit/9be4db035c37c921aefc846c89e286ad8fba56cc))

* docs(tutorial): clean up imports ([`11053b3`](https://github.com/computational-psychology/stimupy/commit/11053b373cf98567a4a786a34d4db464efb57759))

* docs(tutorial): Fix a reference ([`506274e`](https://github.com/computational-psychology/stimupy/commit/506274ef9002cb217f466e60de45f4a7eb6d9bd1))

* docs(topics): Add page on how stimupy is organized ([`0cd3934`](https://github.com/computational-psychology/stimupy/commit/0cd39345f0647648ca37e629fad568cd124c867e))

* docs(tutorial): Move tutorial to separate TOC entry ([`cd3af04`](https://github.com/computational-psychology/stimupy/commit/cd3af04c78c25eef6f0ff4e3243365ee6620da1d))

* docs(tutorial): More verbose tutorial component ([`31c4ae6`](https://github.com/computational-psychology/stimupy/commit/31c4ae69223ba8c507155010ed509c462c4b80b1))

* docs(tutorial): Move composition to separate tutorial page ([`939082a`](https://github.com/computational-psychology/stimupy/commit/939082a5a69f6ccdc087d1e7c5ebb1ae530128c4))

* docs(landing page): use description from README, more detailed cards ([`530dbc0`](https://github.com/computational-psychology/stimupy/commit/530dbc0d2997d4e94ae9a23f6457c05a669099c6))

* docs: README streamlined, in line with manuscript ([`ad8445d`](https://github.com/computational-psychology/stimupy/commit/ad8445d55955044e57ab494ddbbf5889d7b70653))

* docs: Detail on dev installation instructions

Closes #19 ([`506ebf6`](https://github.com/computational-psychology/stimupy/commit/506ebf6ba60e2afc7c2e76434a03ac766bf48cff))

* docs: More detailed contributing instructions ([`97dfa31`](https://github.com/computational-psychology/stimupy/commit/97dfa313f979fd24fc762cb485ec58f6ac293082))

* docs: Get in touch (in addition to contribute) ([`c42cccc`](https://github.com/computational-psychology/stimupy/commit/c42ccccbfa162f4231a18a274a2715476f631716))

* docs(rectilinear): demo rotation of rectilinear stimuli ([`2bd7b98`](https://github.com/computational-psychology/stimupy/commit/2bd7b9861373b0680884c383c03c7ec00e37cc4a))

* docs: consistent docstrings &amp; defaults for `rotation` arguments ([`b441a34`](https://github.com/computational-psychology/stimupy/commit/b441a3437c0b7127b060fc36cbed43d03c90cba4))

* docs: docstring for `combine_masks` ([`c1aa531`](https://github.com/computational-psychology/stimupy/commit/c1aa5314536aef4bb974c7265f201c46875a69bf))

* docs: docstring for `draw_regions` ([`2d2cad2`](https://github.com/computational-psychology/stimupy/commit/2d2cad2b5da102b127f40f21f82355ed5f9dee36))

* docs: docstring for `mask_regions` ([`725eaf0`](https://github.com/computational-psychology/stimupy/commit/725eaf0863a9c72b61d49d7a8f4db2bb74d7181b))

### Feature

* feat(rectilinear): add rotation to rectilinear stimuli ([`0670d6b`](https://github.com/computational-psychology/stimupy/commit/0670d6b07b201fd0f4c0c3f8d4af6480351d2f09))

### Fix

* fix: test bump version ([`bd2cb6f`](https://github.com/computational-psychology/stimupy/commit/bd2cb6fc43a49122508811b5577f2cf928b2dbb6))

### Refactor

* refactor: consolidate and reuse functionality  for dealing with `origin`

The axes and image base grids can differ based on the `origin` argument. We use this in the `image_base`, and should also use this in the plotting, specifically to deal with the `units` argument. Otherwise, how the stimulus is drawn does not match the units being plotted on the axes. Consolidating  this in one place ensure that we can flexibly expand this logic if we want. ([`2fb5f42`](https://github.com/computational-psychology/stimupy/commit/2fb5f4264ec00491a692d22660370040a0a78df3))

* refactor: export `combine_masks`

by adding it to  `components.__all__` ([`6a4b02c`](https://github.com/computational-psychology/stimupy/commit/6a4b02c93cd8b952dbf743d526abaa9cc4a4f8cc))

* refactor(rectilinear): construct rectilinear from obliques

Both for consistency, and to make rectilinear distances rotatable. ([`4d62316`](https://github.com/computational-psychology/stimupy/commit/4d6231657e91edb366b7f70a0afb7ed32e2f6829))

* refactor: update callers of `oblique` / `rotation` ([`a7f8d56`](https://github.com/computational-psychology/stimupy/commit/a7f8d56bebfeba484ffbdc40f2574521e6e17a4e))

* refactor(image_base): `rotation` consistent, extra `oblique_y`

`rotation` argument now consistently rotations counterclockwise from 3 o'clock position (in line with mathematical convention, i.e., unit circle)

Also added an `oblique_y` metric, orthogonal to `oblique` (which is implicit `oblique_x`) ([`8e17857`](https://github.com/computational-psychology/stimupy/commit/8e17857975077f0eaf70edcd4d119c5dcfe5aab4))

* refactor: update import of `combine_masks` ([`53dea7d`](https://github.com/computational-psychology/stimupy/commit/53dea7d83a350258f539b7f0cdd59c95f6e65c99))

* refactor: move `combine_masks` to `components` ([`31dff51`](https://github.com/computational-psychology/stimupy/commit/31dff51dd770d038ff9a7dbaad2b1a8e6d198d94))

* refactor: rename `mask_elements` -&gt; `mask_regions` ([`090f0d7`](https://github.com/computational-psychology/stimupy/commit/090f0d7d3c30a17c36fefc4c225d0a413eb8f80f))

### Unknown

* v0.100.0

Automatically generated by python-semantic-release ([`3d89415`](https://github.com/computational-psychology/stimupy/commit/3d894158c6a13eae25ce56c7956bd1006deb06d7))

* Merge pull request #77 from computational-psychology/dev

Dev: refactor, documentation, improve build ([`bc1289c`](https://github.com/computational-psychology/stimupy/commit/bc1289cb5c53d7476aa3f3581a84101e7bc887e3))

* Merge branch `build_release` into dev ([`3acc86f`](https://github.com/computational-psychology/stimupy/commit/3acc86f14de4beb4b2d3673a399bbad42d6a898f))

* Merge branch `docs` into dev ([`6c62384`](https://github.com/computational-psychology/stimupy/commit/6c623840e5ed3f55cda81791559336a518c2792a))

* Merge branch `refactor` into dev ([`5992727`](https://github.com/computational-psychology/stimupy/commit/599272740c0651ae9853af4ede480cb04d50fb66))

* Merge pull request #68 from computational-psychology/dev_version

Implement versioning ([`4f8a889`](https://github.com/computational-psychology/stimupy/commit/4f8a8897bd19bf3030cb0a8873fd03bf98a26de5))

* v0.99.1

Automatically generated by python-semantic-release ([`ebda6b3`](https://github.com/computational-psychology/stimupy/commit/ebda6b376ced6b3e9e6f081845a5a972d7cd8905))

* Merge pull request #62 from computational-psychology/feat_consistent_todorovics

fix(todorovics): Consistent behavior for `todorovics.rectangle` and `.cross`

Closes #61 ([`616e96d`](https://github.com/computational-psychology/stimupy/commit/616e96d74c16de9bba3b115d6a94b4828f59117d))

* closes #61; consistent todorovic rectangle and cross behavior ([`ff9b47f`](https://github.com/computational-psychology/stimupy/commit/ff9b47f5604f77130c305ef7fc8eb5343396cd9b))


## v0.99.0 (2023-03-29)

### Unknown

* Update issue templates ([`5a98fb4`](https://github.com/computational-psychology/stimupy/commit/5a98fb467ff8895bbd594bb4fbb37061c190cd8a))

* Merge pull request #60 from computational-psychology/feat_check_demos

closes #52; double check all demos ([`0d74b39`](https://github.com/computational-psychology/stimupy/commit/0d74b39ff87a0d8356aa1ebe3d2e2b5c696036bf))

* autoformatting ([`d382596`](https://github.com/computational-psychology/stimupy/commit/d382596a44bff939b505f55526dec513728492a8))

* updated some sbcs-demos args; and fixed bugs in dotted sbcs ([`941cbaa`](https://github.com/computational-psychology/stimupy/commit/941cbaa7bd76eebebd2e31ee32180cb304409c38))

* fixed args in mondrians demos, and fixed bug in mondrians ([`db6a3d4`](https://github.com/computational-psychology/stimupy/commit/db6a3d41dc87fe2bf29be7bbe4ef7b3e16e7188b))

* updated one arg in demos-gabors ([`6e57781`](https://github.com/computational-psychology/stimupy/commit/6e5778145c376ff898a55719d10f02b0ea6cb2c0))

* autoformatting ([`df0f87f`](https://github.com/computational-psychology/stimupy/commit/df0f87fc65eaaf51cc78c77f667f45060e1e31f1))

* increased frequency in waves-demo because of angular-wave ([`af053df`](https://github.com/computational-psychology/stimupy/commit/af053df88f9ab6658d6be76171e7877ba24ab19a))

* had to rename one arg in demos-shapes ([`9a2ede4`](https://github.com/computational-psychology/stimupy/commit/9a2ede429d28559501bc840e1bece0c9d2233379))

* fixed small bug in radials ([`1f6e790`](https://github.com/computational-psychology/stimupy/commit/1f6e790e0a5f78887cade79154ed175b961808bd))

* fixed tiny bug in frames ([`8a4d667`](https://github.com/computational-psychology/stimupy/commit/8a4d66705517c6e1f0fdcb6f4b2be706a50f4732))

* updated edges-demos (renamed functions, and added missing args) ([`cd881f8`](https://github.com/computational-psychology/stimupy/commit/cd881f897d242fbef6aa173fc3659ad1754ba0b5))

* removed non-existent angular-components-functions from demo; added segments; fixed bugs in segments ([`de9c765`](https://github.com/computational-psychology/stimupy/commit/de9c765db8c0c94284ffccad99fc60b44b9289b9))

* removed old demos ([`0fcf6a3`](https://github.com/computational-psychology/stimupy/commit/0fcf6a3b6daffa761fe469f46ac156cbde61db57))

* Merge pull request #59 from computational-psychology/feat_yaz

closes #51; removed stripe intensities from yazdanbakhsh ([`46e6520`](https://github.com/computational-psychology/stimupy/commit/46e6520dfd7ab32976bfd7c92abfa0fdfe2f4703))

* closes #51; removed stripe intensities from yazdanbakhsh ([`51cbe75`](https://github.com/computational-psychology/stimupy/commit/51cbe755686428e71f9a4ed3181e64baa52379ad))

* Merge pull request #58 from computational-psychology/feat_clip

closes #42; added clipping and fixed some defaults ([`c422917`](https://github.com/computational-psychology/stimupy/commit/c42291750b260a79baf2b6a5fadfee672f4149b2))

* closes #42; added clipping and fixed some defaults ([`02d0081`](https://github.com/computational-psychology/stimupy/commit/02d00815452df9e2ca134dcd198295213ce1b8a2))

* Merge pull request #57 from computational-psychology/feat_rename_masks

closes #13; renamed shape_masks and grating_masks in checkerboard ([`16f15d6`](https://github.com/computational-psychology/stimupy/commit/16f15d601d95f9c342a1ad22d4495684c186e9b5))

* closes #13; renamed shape_masks and grating_masks in checkerboard ([`f6c7636`](https://github.com/computational-psychology/stimupy/commit/f6c7636ac63d3965b5fe813cbf452f93c963ddd7))

* Merge pull request #55 from computational-psychology/feat_two_sided

closes #40; renamed two-sided sbcs ([`3c73c5d`](https://github.com/computational-psychology/stimupy/commit/3c73c5de11131f3c861cb3c00824c9c1ffecd11b))

* closes #40; renamed two-sided sbcs ([`95d0b15`](https://github.com/computational-psychology/stimupy/commit/95d0b159eda3b5c95ee5b0dcfbd65fd8785502b6))

* Merge pull request #54 from computational-psychology/manuscript

Update JOSS manuscript ([`bad3d76`](https://github.com/computational-psychology/stimupy/commit/bad3d76adf3c42ea1effb61bda824d66e076cebe))

* Also compile pdf on main ([`29f0343`](https://github.com/computational-psychology/stimupy/commit/29f0343d66a192d572b33d3ddedfa7161d92a00c))

* Un-typeset a list ([`af875e2`](https://github.com/computational-psychology/stimupy/commit/af875e238d7be3e4c1ab23b8e41663adb53593b1))

* Update date ([`dc8b69a`](https://github.com/computational-psychology/stimupy/commit/dc8b69a478df62a50048d1e6b5438ab55b08b55f))

* Umlaut affiliation ([`06a3496`](https://github.com/computational-psychology/stimupy/commit/06a34963c8741a84a145a79420f2a2d6c7ce88bf))

* Change link noise ([`4172d1b`](https://github.com/computational-psychology/stimupy/commit/4172d1bb9a546680acd781a77ecc65540a2fcc24))

* Fix bib ([`cf7381c`](https://github.com/computational-psychology/stimupy/commit/cf7381c439abdf07c5785929e637801daab1d81f))

* Bugfix: figure ref ([`df541c2`](https://github.com/computational-psychology/stimupy/commit/df541c22359d46a375305e14efe0b79dedcc18c7))

* Typeset another list ([`27bd124`](https://github.com/computational-psychology/stimupy/commit/27bd1240b1f9629762e8e2a9914e6d8d8d54a187))

* Typeset list ([`11bb47e`](https://github.com/computational-psychology/stimupy/commit/11bb47e7d3ae1d28e82ebb2ac74f41cbe9b3ad7d))

* Monospace `stimupy` ([`352583d`](https://github.com/computational-psychology/stimupy/commit/352583dad30a69346bb64e5807f4523abd9f0d05))

* Add links and typeset list ([`fdcc03d`](https://github.com/computational-psychology/stimupy/commit/fdcc03d1f517ee78d17202d835c69b2c7aed9538))

* Move and reference figure(s) ([`392e5eb`](https://github.com/computational-psychology/stimupy/commit/392e5ebf48741d29c34173c6ac7ad13dfe2b118c))

* Add Murray2020 to bib ([`b2d3a2d`](https://github.com/computational-psychology/stimupy/commit/b2d3a2d74390ab309e6582d52d88bcb93a05c133))

* GitHub workflow for generating PDF ([`df05544`](https://github.com/computational-psychology/stimupy/commit/df055446ad1bf75deade09d97e69ee3f72e4c305))

* Update title ([`38a12a6`](https://github.com/computational-psychology/stimupy/commit/38a12a6c1c0ede44b43d8d5cbf95945bffb1e45a))

* Update references ([`485fc9a`](https://github.com/computational-psychology/stimupy/commit/485fc9aeb80da1106258b824fdd8482c82e67749))

* Add figures manuscript ([`9be796a`](https://github.com/computational-psychology/stimupy/commit/9be796a7b669d34f46708e04d5ed39348f20be88))

* Latest version of manuscript ([`87464bf`](https://github.com/computational-psychology/stimupy/commit/87464bf5e17971c80892287030e3556cad1c3e7d))

* Merge pull request #46 from computational-psychology/docs_demos

Docs: add remaining demos (still a few demos missing for stimuli.gratings) ([`90a29a2`](https://github.com/computational-psychology/stimupy/commit/90a29a29e0318619d9fa73fc37098a47468f27ba))

* Merge branch `main` into docs_demos ([`b63e43d`](https://github.com/computational-psychology/stimupy/commit/b63e43d8b9569e7634bcac90f09a9710477bc2a0))

* Merge pull request #50 from computational-psychology/feat_whites

Bugfix:  `whites` ([`23a23b7`](https://github.com/computational-psychology/stimupy/commit/23a23b7d56b0916d4507f4de66b2f7b468a32f71))

* Lint &amp; format ([`857c3e0`](https://github.com/computational-psychology/stimupy/commit/857c3e09e642666d3e32f755a06fca31274dc9c0))

* Docs: update demo `whites.yazdanbakhsh` ([`a44d58f`](https://github.com/computational-psychology/stimupy/commit/a44d58f298b7f1f266ba2750e7dc21ae19ae8bd1))

* Docs: update demos `whites.anderson`, `.howe` ([`5d49139`](https://github.com/computational-psychology/stimupy/commit/5d49139a99be2b2ef8da8f92187b2747e4f3d7a7))

* Tests: Regenerate RHS2007 ground truth, slight change WE_anderson, _howe ([`4b91761`](https://github.com/computational-psychology/stimupy/commit/4b9176181f883d68c8e466b73fdaa36806de012a))

* Docs: update demo `whites.yazdanbakhsh` ([`6d1109d`](https://github.com/computational-psychology/stimupy/commit/6d1109daa518fe4e51cb2e3f5d6e63e3d16ff93f))

* Rewrite `whites.yazdanbakhsh`

Uses `components.rectangles` to content-aware place gaps. Can then also handle multiple target heights ([`98bbb0b`](https://github.com/computational-psychology/stimupy/commit/98bbb0b49cf98f633bc4126d1c4474078646bc20))

* Docs: update demos `whites.anderson`, `.howe` ([`0292b9d`](https://github.com/computational-psychology/stimupy/commit/0292b9df49d15fc654eef39a351f7cee3df2e4be))

* Bugfix: whites_generalized returns actual lists of target params

Previously was just `itertools.cycle`-objects, which are harder to work with ([`b6fafff`](https://github.com/computational-psychology/stimupy/commit/b6fafff963916124039e68971e77304d92431d39))

* `whites.anderson` draws stripes as `rectangle`s ([`d7b05c9`](https://github.com/computational-psychology/stimupy/commit/d7b05c91b580374b9d53e0f2b2c0885953647c02))

* Util for combining masks ([`9ae1b74`](https://github.com/computational-psychology/stimupy/commit/9ae1b745776f6f8e1c7f0a286218f815abeb06c1))

* `white_two_rows` also outputs target idc separately ([`63e694d`](https://github.com/computational-psychology/stimupy/commit/63e694db7b9d625a0eb11b790668e229659f6784))

* Draw targets in `whites` as `rectangle`s ([`c84a1a1`](https://github.com/computational-psychology/stimupy/commit/c84a1a12ecc8dd6f6c4562037387d86771c339e1))

* Bugfix: example white_yazdanbakhsh ([`6b15eaa`](https://github.com/computational-psychology/stimupy/commit/6b15eaa695565f9970a832f70c509330bfe9e16b))

* Add `clip=True` to example `white_radial` ([`db9c0b3`](https://github.com/computational-psychology/stimupy/commit/db9c0b350f7ed5968702c8292b826621f4ba9b45))

* closes #48; fixed white issues ([`47b4b50`](https://github.com/computational-psychology/stimupy/commit/47b4b50f11efc4c778d0b07c76cfe71e5ceaef4e))

* Merge pull request #49 from computational-psychology/feat_todorovics

Bugfix: Todorovics ([`37d8535`](https://github.com/computational-psychology/stimupy/commit/37d8535df70aff6721819c15a50da8f2ae197b21))

* also updated todo-equal-target-mask ([`4d500d2`](https://github.com/computational-psychology/stimupy/commit/4d500d22b6ab8a63b03f62133281aae4edf51b77))

* closes #43; fixed all bugs in todorovics ([`b162153`](https://github.com/computational-psychology/stimupy/commit/b16215301fcd8b4343f3e4b9c0960dc22eb7dfdd))

* added whites demos ([`1d7246a`](https://github.com/computational-psychology/stimupy/commit/1d7246ac204b2cffe05c9ba29c32f7a94cd0b8b5))

* added demos for all three plaid stims ([`0672974`](https://github.com/computational-psychology/stimupy/commit/067297441e57ae93df2c1b06ef2b6596ed6579d5))

* Merge pull request #45 from computational-psychology/fix_angular_freq

Bugfix: angular frequency in cycles per image ([`acef103`](https://github.com/computational-psychology/stimupy/commit/acef103722ae2c94c555a1deddd51b026e1a06fc))

* Merge branch `docs_demos` of github.com:computational-psychology/stimupy into docs_demos ([`35524d8`](https://github.com/computational-psychology/stimupy/commit/35524d82c5bea9925a2c8bb7dd3bbab5b631c56f))

* added todorovics-demos ([`64925d4`](https://github.com/computational-psychology/stimupy/commit/64925d4c6397aa304895cd19e103907602f42250))

* Bugfix: angular frequency in cycles per image ([`052d391`](https://github.com/computational-psychology/stimupy/commit/052d391f26b77040e803a2abff0f786d0a038d32))

* Demos: `stimupy.waves.angular` ([`826e851`](https://github.com/computational-psychology/stimupy/commit/826e851027e001cae7da6c34c08f513afa191030))

* Demo: stimuli/waves ([`a2c45a4`](https://github.com/computational-psychology/stimupy/commit/a2c45a42bf8f6af04145d93bea91ea496a655cf1))

* Merge pull request #41 from computational-psychology/feat_noise_utils

Moving noise-utils to noise-init ([`fcf4717`](https://github.com/computational-psychology/stimupy/commit/fcf4717d66a62fc96f4d7042d8ba58a2951ee685))

* Merge branch `main` into feat_noise_utils ([`3b78791`](https://github.com/computational-psychology/stimupy/commit/3b78791c20c1c5f4dd8da646666ff80574f82784))

* Demo: stimuli/SBCs ([`2ac4162`](https://github.com/computational-psychology/stimupy/commit/2ac4162e25256cdec097c77f894237f1ba9fbe25))

* Merge pull request #35 from computational-psychology/feat_waves

Waves, primarily angular ([`f42bb0e`](https://github.com/computational-psychology/stimupy/commit/f42bb0ebb56a2082f3f08bdb6ae071d7d4d0341f))

* closes #33; moved noise-utils to noise-init ([`2fdfd54`](https://github.com/computational-psychology/stimupy/commit/2fdfd54510aa52c55592fb86943403cbcf24c0da))

* Bugfix overview `wedge` ([`f1e5a9d`](https://github.com/computational-psychology/stimupy/commit/f1e5a9dacad30637e0182469ff01b99beb848fd8))

* Merge branch `main` into feat_waves ([`799fb5b`](https://github.com/computational-psychology/stimupy/commit/799fb5b6613bb64a5abc696d95e191b7b93d9922))

* added gabors to __all__ in plaids ([`21b4d8d`](https://github.com/computational-psychology/stimupy/commit/21b4d8d750916c526cc80638fc716f461ed3ed68))

* closes #22; closes #26; fixed problem with (angular) waves ([`418458a`](https://github.com/computational-psychology/stimupy/commit/418458aba8e88ef2891f1b829d0bb2fd8a966fb8))

* Merge pull request #34 from computational-psychology/dev

Minor issues ([`1c76f9c`](https://github.com/computational-psychology/stimupy/commit/1c76f9c194ea016d7d356f42637f72ebe27d7ec6))

* Docstrings `utils.plotting` ([`24ea263`](https://github.com/computational-psychology/stimupy/commit/24ea2638a38bf1bc2619ed68972ed63041045804))

* `units` argument to `plot_stim` (and callers)

Replaces `extent_key`, but serves the same purpose. Can put in either:
- `pixels` (syn: `px`, `pix`)
- `degrees` (syn: `deg`)
- another str  that is a key in `stim`-dict, like current `extent_key` arg

Closes #9 ([`550a22e`](https://github.com/computational-psychology/stimupy/commit/550a22ec280e37346a974a98de0978599aa05d92))

* Merge branch `main` into dev ([`1db171a`](https://github.com/computational-psychology/stimupy/commit/1db171a6830e676d5950686ce14f593862506ead))

* Docs: bugfix tutorial - update references to `stimuli` (from `illusions`) (#36)

And update API paths ([`3091cc3`](https://github.com/computational-psychology/stimupy/commit/3091cc3771d0786da8fc3b2f1ed5f4b58e23741c))

* fixed and updated mondrians; corrected error msg in radials ([`2f9105c`](https://github.com/computational-psychology/stimupy/commit/2f9105cf52c61d4d716e56d202e6339160e1a9a4))

* Bugfix: overview `gabors` ([`2187127`](https://github.com/computational-psychology/stimupy/commit/21871278ad111d761310e34f8b4fe5f26526ac1f))

* Change imports in `components` ([`4b2c1eb`](https://github.com/computational-psychology/stimupy/commit/4b2c1ebc2ec9521cf844abf911f5223a7cc368d6))

* Bugfix `components.overview` should exclude exported functions ([`316a4c5`](https://github.com/computational-psychology/stimupy/commit/316a4c5c24dac696c29a9e192c472af66e26d613))

* Default to `intensity_background=0.0` for some components ([`8dc1fbf`](https://github.com/computational-psychology/stimupy/commit/8dc1fbf50296a81f226f2c7c355feef5fd9464f9))

* Rename `components.edges`-functions

Now all `edges.step()` etc. ([`f33113a`](https://github.com/computational-psychology/stimupy/commit/f33113ab926c3f54d84723af9994b8ebc5fb62d4))

* Fix &amp; update overviews for all modules

Closes #29, #30, #32
Bugfix: explicit import and export in `noises` ([`2cfc77d`](https://github.com/computational-psychology/stimupy/commit/2cfc77da6355bfbd09eb1b23c0c12da5ae8d2abf))

* Update `components.waves` example params ([`2621ebf`](https://github.com/computational-psychology/stimupy/commit/2621ebff92152a800c7178aed91a81541875be93))

* Update overview ([`cc8f0a6`](https://github.com/computational-psychology/stimupy/commit/cc8f0a66853eeb27737661b6a22ec478803d25c5))

* Add `staircase_`s to `stimuli.waves` ([`27d10d0`](https://github.com/computational-psychology/stimupy/commit/27d10d0903467bc9512590e43ab8dc66dc1b54b5))

* Update how `components.staircase` deals with intensities ([`c6fe298`](https://github.com/computational-psychology/stimupy/commit/c6fe29838604750edbfbe8dfab63c5612bf57a49))

* Remove `angulars.grating` ([`f1b5a17`](https://github.com/computational-psychology/stimupy/commit/f1b5a17c06368a4ca7d88c09ed7ca69427eb7291))

* Use `waves.angular` in `pinwheel` ([`7f53ed7`](https://github.com/computational-psychology/stimupy/commit/7f53ed70c6634310d1213236fc0e8ed4fb830b23))

* Bugfix: adjust distances properly for angular waves ([`a3d3322`](https://github.com/computational-psychology/stimupy/commit/a3d33224ff54414c6baa3b4b93533b5603e48583))

* Add defaults to `components.waves` ([`1c488b0`](https://github.com/computational-psychology/stimupy/commit/1c488b02ffd154fbc2374a13133a3967981df75b))

* `benarys` raises error if targets do not fit into stim

closes #17 ([`fdb03a6`](https://github.com/computational-psychology/stimupy/commit/fdb03a6037aea8a77a444831d6635a224c696fb7))

* Gabor args consistent with wave args, and added function to create plaids from any kind of waves or gabors

Closes #31, Closes #21 ([`71f5348`](https://github.com/computational-psychology/stimupy/commit/71f5348aa1d8f54491b5b37a003c696c3a17e35b))

* Merge pull request #28 from computational-psychology/dev

Closing some smaller issues ([`b1dfd47`](https://github.com/computational-psychology/stimupy/commit/b1dfd475238d5b7763bed90bf5d366fc584555e8))

* Also rename `rectilinear` (from `cityblock`) in demos ([`a26defc`](https://github.com/computational-psychology/stimupy/commit/a26defc27195116635fcf8ba395bc4d5e6a079bf))

* Also update tests... ([`9e3a25e`](https://github.com/computational-psychology/stimupy/commit/9e3a25e291fd33233ce4d6594bae856b4b0595b0))

* Unify structure for `overview`s

For each module, `overview()` generates a dict of stim_dicts, with some example stimuli.
For &#34;parent&#34;-modules, they run the `overview()` for each of their submodules, and concatenate.
`plot_overview()` simply passes this to `plot_stimuli`, as a nice shorthand. ([`f6b115a`](https://github.com/computational-psychology/stimupy/commit/f6b115a3828fdf8aa8170435a2b27ee9c23274b8))

* autoformatting ([`937c832`](https://github.com/computational-psychology/stimupy/commit/937c8326365f986bb9cd32557b978b93c31d9b18))

* closes #27; renamed cityblock to rectilinear ([`523f4d1`](https://github.com/computational-psychology/stimupy/commit/523f4d1ebf2d001947e04b96a139dd66ecd29cd5))

* closes #14; contrast_contrast new defaults for target_shape and alpha are None ([`0fd8b4e`](https://github.com/computational-psychology/stimupy/commit/0fd8b4ef55cdf862a78b9dcc7c280068e2eb7873))

* closes #15; fixed bug ([`c1bbf8d`](https://github.com/computational-psychology/stimupy/commit/c1bbf8d617a63e0c400dc709f88db7842ee66074))

* closes #16; bessel raises error if frequency=None ([`86020c9`](https://github.com/computational-psychology/stimupy/commit/86020c93bd4cf98c19c779fa62fc738eb059e467))

* Bugfix: output visual_size, ppd in `gratings.on_grating`

Closes #18 ([`52b57de`](https://github.com/computational-psychology/stimupy/commit/52b57de00d67b959508eedfb162314cdce7902dc))

* Rename `rotated` distance metric to `oblique`

Closes #10 ([`4eec2de`](https://github.com/computational-psychology/stimupy/commit/4eec2de9b15797e94930709370b8078a32ecaffb))

* Docfix: path to demos for `noises` ([`a8c8e02`](https://github.com/computational-psychology/stimupy/commit/a8c8e02a942289244123359f94fde8280d97c944))

* `distance_metric` to refer to `image_base` components

and `rotation` to refer to other `orientations`

Closes #8 ([`9f9825e`](https://github.com/computational-psychology/stimupy/commit/9f9825eaab136a7701309d894d01d093843ba07e))

* Merge pull request #23 from computational-psychology/dev_reorganize

Reorganize stimulus functions ([`c7c2754`](https://github.com/computational-psychology/stimupy/commit/c7c2754d56f7eaf42e455720751ecab08ccef28e))

* Merge pull request #24 from computational-psychology/feat_demos

Reorganized (and updated) existing demos to fit new organization ([`cd8f644`](https://github.com/computational-psychology/stimupy/commit/cd8f644239cd7ac40602cd7a30a0e7faea8a89cc))

* Remove demos `sinewave`, `squarewave` from `components.frames` ([`6da1150`](https://github.com/computational-psychology/stimupy/commit/6da11501fc3bbc40183c0f7a00f4f4a538b7e51b))

* Bugfix: demo `pinwheels` name ([`349bba8`](https://github.com/computational-psychology/stimupy/commit/349bba89b211a9f03a2b4057c73e4a0f6612b304))

* Rename and update demo `components.radials` ([`266b847`](https://github.com/computational-psychology/stimupy/commit/266b84732d40fef7872594a6d4256004aca4e64d))

* Move demo `bessel` to `waves` ([`34c191a`](https://github.com/computational-psychology/stimupy/commit/34c191ae941d7c1efdb68093512bea0ff1a7fae0))

* Rename and update demo `components.waves` ([`aeed9f8`](https://github.com/computational-psychology/stimupy/commit/aeed9f86a5c270899346cf4d30048385a3ed4ecc))

* Extract demo `plaids` ([`9b303b9`](https://github.com/computational-psychology/stimupy/commit/9b303b96c787896ffa25a0181eeaa0b4d162011a))

* Extract and move demo `gabors` ([`1b07da8`](https://github.com/computational-psychology/stimupy/commit/1b07da8943f78aec060f9b1727db5cff8305a294))

* Fix demo `stimuli.gratings` ([`d441aa9`](https://github.com/computational-psychology/stimupy/commit/d441aa97d7c6f55149b37de0179964d721f6a49a))

* Start demo `stimuli.waves`, move `gratings.square_wave` there ([`8c1a7cc`](https://github.com/computational-psychology/stimupy/commit/8c1a7cc3f80b2d625e5496121d14e2885582bfba))

* Combine and update demos Mondrians ([`ff2ffef`](https://github.com/computational-psychology/stimupy/commit/ff2ffef0313fa0f06e6b2d21f3b6ae2f0aa1dd47))

* Remove obsolete `components.checkerboards` demo ([`33683ce`](https://github.com/computational-psychology/stimupy/commit/33683ce568b2e49372f92cc9c5a4b07877e7eeaf))

* Move rectangular bullseyes ([`d4cf197`](https://github.com/computational-psychology/stimupy/commit/d4cf197668b04537c513b9b0472594116a30046b))

* Move rectangular rings ([`dbefad6`](https://github.com/computational-psychology/stimupy/commit/dbefad6274aee9914ddda66c28757ddf82add0fd))

* Move circular rings ([`27a1791`](https://github.com/computational-psychology/stimupy/commit/27a1791ef6e24c088bf35f56f86ae932441d93b6))

* Move circular bullseyes ([`1900455`](https://github.com/computational-psychology/stimupy/commit/19004556a2f0301becc7007a19ddcad378cca26c))

* Update README ([`66ce116`](https://github.com/computational-psychology/stimupy/commit/66ce1163efa05bc2a0a97462ce19973988348e39))

* Rename &amp; autosummary template ([`f655e34`](https://github.com/computational-psychology/stimupy/commit/f655e3440d76f7130dd17237481e1c2364310847))

* Auto-rename `illusions` -&gt; `stimuli` ([`6613ddc`](https://github.com/computational-psychology/stimupy/commit/6613ddcd8b1b38b5d73949bd403597b7e1c43cbd))

* Rename &amp; fix `pinwheels` (fka `angulars`) ([`2dcd181`](https://github.com/computational-psychology/stimupy/commit/2dcd1812d3b3a0a7b25d418a36403a8218912293))

* Rename dir `illusions` -&gt; `stimuli` ([`9e03fb1`](https://github.com/computational-psychology/stimupy/commit/9e03fb1d2908af6a52f36b008580f024e852c54b))

* (auto)format ([`969ae57`](https://github.com/computational-psychology/stimupy/commit/969ae577d0e9e320466877256d2efa74233a300f))

* Angular waves, currently not working ([`a237494`](https://github.com/computational-psychology/stimupy/commit/a23749445415c998b5850079436815ead6189d71))

* Bugfix: imports ([`cce3333`](https://github.com/computational-psychology/stimupy/commit/cce3333eb6b170cdb5aab0142a7904467bc3d6e2))

* Add top-level `__main__` ([`cd0b6ec`](https://github.com/computational-psychology/stimupy/commit/cd0b6ec133ce411160c62f2f7cf7915301820f8c))

* Move all stimuli into `stimuli` subdir (though import up) ([`109064b`](https://github.com/computational-psychology/stimupy/commit/109064bd412cadadd07f54b615344bd28bc0861b))

* Bugfix: gabor example ([`c2d2ef2`](https://github.com/computational-psychology/stimupy/commit/c2d2ef2bc1f22348f719cbb005268b8a462d7933))

* Bugfix: checkerboard examples ([`30ba15a`](https://github.com/computational-psychology/stimupy/commit/30ba15aaf773b121113c23d3acf241a08b38ab54))

* Remove `illusions` ([`1440793`](https://github.com/computational-psychology/stimupy/commit/1440793d4c312529fb89dee68bd7ab21e20446c8))

* Move `illusions.angulars` -&gt; `pinwheels` ([`26bba52`](https://github.com/computational-psychology/stimupy/commit/26bba52ff51f5b1e532b053f495fb659a2817ef5))

* Merge branch `feat_cityblock` into dev_reorganize ([`2969f95`](https://github.com/computational-psychology/stimupy/commit/2969f95f77b623363ee3879a485de1dc6be5d726))

* Remove obsolete `illusions.frames` ([`59d1920`](https://github.com/computational-psychology/stimupy/commit/59d192045439641e887107a896ece2c7032c7a11))

* Bullseyes from `rings` ([`f5690c6`](https://github.com/computational-psychology/stimupy/commit/f5690c641ebb7f23766a8b39487593db26a0b8da))

* Bugfix: add `origin` to `rings.rectangular_` ([`d977fbb`](https://github.com/computational-psychology/stimupy/commit/d977fbbaa6e2c7d253bb30bb41a5659a613a516b))

* Move generalized `frames` to `rings.rectangular_generalized` ([`9ece5c8`](https://github.com/computational-psychology/stimupy/commit/9ece5c8d05c38430ebe14215a290ee213738bbf8))

* Move `illusions.frames.rings` into `rings.rectangular`, `.rectangular_two_sided` ([`8fabb3e`](https://github.com/computational-psychology/stimupy/commit/8fabb3e165d21c72aafdcd53b29341bfef199056))

* Cleanup `components.frames` ([`ecd652f`](https://github.com/computational-psychology/stimupy/commit/ecd652f3e6718f3ae85b403ebb929e17be226436))

* Replace `frames.frames` by `waves.square_cityblock` ([`a2c4d45`](https://github.com/computational-psychology/stimupy/commit/a2c4d45d53b57b57e130c2358bb71ce51167f38b))

* Add `clip`ping to `waves._cityblock` ([`ee1420f`](https://github.com/computational-psychology/stimupy/commit/ee1420f59c5fb622dfcd9c269ad980f5ab92d41f))

* Add Cityblock waves ([`1fec019`](https://github.com/computational-psychology/stimupy/commit/1fec019c204a40a3f46b082bb0c74aee3193e4b9))

* Merge branch `feat_radial` into dev_reorganize ([`b316b5b`](https://github.com/computational-psychology/stimupy/commit/b316b5b05aea092b8f417cdc1976538ed8df1efe))

* Rename `components.circulars` -&gt; `components.radials` ([`3c3d434`](https://github.com/computational-psychology/stimupy/commit/3c3d43402a24eaf58ccd6ae9f20d2d8eeb6993ac))

* Cleanup `components.circulars` ([`02a66e8`](https://github.com/computational-psychology/stimupy/commit/02a66e8e620b5ffcf99ba38acb608851fd4de033))

* Split `circulars` into `bullseyes`, `rings` ([`eca182a`](https://github.com/computational-psychology/stimupy/commit/eca182a771f670742c036475ef7a750b10ce1475))

* Replace `circular.rings` by `waves.square_radial` ([`c30c9e1`](https://github.com/computational-psychology/stimupy/commit/c30c9e191aac89b8cc30e8b690804e16aae0fc82))

* Circular White's uses (is) `waves.square_radial` ([`2aa7623`](https://github.com/computational-psychology/stimupy/commit/2aa762378d87fa9c4cc3964546280b70c924694f))

* Add `clip`ping to `waves._radial` ([`2dd9297`](https://github.com/computational-psychology/stimupy/commit/2dd9297256c19c5bab2912360b6a18b4b444d422))

* Bugfix: default origin for radial gratings ([`4b5a48c`](https://github.com/computational-psychology/stimupy/commit/4b5a48c66e28eab32f5112c8e38789acd105eb6f))

* Add `waves.sine_radial`, `.square_radial` ([`a13bd2f`](https://github.com/computational-psychology/stimupy/commit/a13bd2f8c55cc47c29388f121d8bbbc4963bb2dc))

* Extract function for adding targets to waves/gratings ([`3d10e7c`](https://github.com/computational-psychology/stimupy/commit/3d10e7cd3a93876f6ce1337ddc9d101d5f6e3042))

* Cornsweets as toplevel stimulus module ([`3f9a52f`](https://github.com/computational-psychology/stimupy/commit/3f9a52fe9f451f55572e99862694dc91f1fae860))

* Checkerboards as toplevel stimulus module ([`1e66d3d`](https://github.com/computational-psychology/stimupy/commit/1e66d3d05526bf8a53e17a233f168434d148b8ad))

* Absorb `bessel` into `components.waves` ([`69f5c2f`](https://github.com/computational-psychology/stimupy/commit/69f5c2f54c0f9376f2950707f35ec07603325292))

* Absorb `components.checkerboards` into `stimupy.checkerboard` ([`8b3db94`](https://github.com/computational-psychology/stimupy/commit/8b3db94e72ed88fde6eb5b9ff89b28c28acc280f))

* Merge branch `feat_waves_gratings` into dev_reorganize ([`05c1db1`](https://github.com/computational-psychology/stimupy/commit/05c1db104c7377d7ebbf58c482e7a3605f78d763))

* Remove deprecated `components.gratings` ([`d73500c`](https://github.com/computational-psychology/stimupy/commit/d73500ce7e11800db8d08cc6643beb3280445a42))

* Update `test_gratings` -&gt; `test_waves` ([`a1b4d88`](https://github.com/computational-psychology/stimupy/commit/a1b4d8820e00b45bc6d553214c177aa2693d09bb))

* Checkerboard uses `components.waves` instead of `components.gratings` ([`d2313b4`](https://github.com/computational-psychology/stimupy/commit/d2313b41754658934c6f1515059d8afaa1686785))

* Whites uses `stimupy.gratings` instead of `components.gratings` ([`828e2bf`](https://github.com/computational-psychology/stimupy/commit/828e2bf9cf034aeacff99716760a4be55032c234))

* Plaid uses `components.waves` instead of `components.grating` ([`add14f1`](https://github.com/computational-psychology/stimupy/commit/add14f1b2fe26279ec7e3bfd123b5262854e4c40))

* Update ModelFest ([`77092ac`](https://github.com/computational-psychology/stimupy/commit/77092ac6c31ff1864f087bdf21ad08f09c9b4c7e))

* Gabors uses `components.waves` instead of `components.gratings` ([`58a5d17`](https://github.com/computational-psychology/stimupy/commit/58a5d175d3a49a08e24dd18cc4253ff83fe8fe2b))

* Move `components.gratings.staircase` to `components.waves.staircase`

And make flexible: can be applied over any distance metric ([`bc0837a`](https://github.com/computational-psychology/stimupy/commit/bc0837a285f5b42b7cb8774e53d045557710324c))

* Gratings as toplevel stimulus module ([`3e66f31`](https://github.com/computational-psychology/stimupy/commit/3e66f314e6ec3edaee5863810bd7b811766c79c9))

* Update all other `stimupy.gratings` functions

Now all use the `stimupy.waves` for the underlying waves ([`ee57de8`](https://github.com/computational-psychology/stimupy/commit/ee57de8ef7a6c0addac0ac200b7b0cbf97327af8))

* Swap phase order ([`3dbad3a`](https://github.com/computational-psychology/stimupy/commit/3dbad3aba6e52bd1932c694bba0e1923559803ff))

* 0-based `grating_mask`s ([`0b714cd`](https://github.com/computational-psychology/stimupy/commit/0b714cdab4a7720bb0e024cea91e38f67384ebee))

* Adjust examples ([`29f14d9`](https://github.com/computational-psychology/stimupy/commit/29f14d9cb1220bce7985a9fe864e6a6c799bdb81))

* Adjust fudgefactor... ([`8e6b920`](https://github.com/computational-psychology/stimupy/commit/8e6b920a960536887a4fc53679c2a57131fa912d))

* Bugfix: key `target_mask` in `waves._linear` ([`461f593`](https://github.com/computational-psychology/stimupy/commit/461f5932d1821321c43740457e04d56c4e987659))

* Replace `gratings.square_wave` with `waves.square_linear` ([`ae195ef`](https://github.com/computational-psychology/stimupy/commit/ae195efe75189894554296386c0d1269cd8f0b18))

* Better `grating_mask` in `components.waves`

Clarified code.
Slight offset on `edges`, so that regions &#34;round-down&#34; ([`1c09044`](https://github.com/computational-psychology/stimupy/commit/1c090443b77fcfc218aca7d4c563b3244a54926a))

* Better mask in `waves` ([`8f958bf`](https://github.com/computational-psychology/stimupy/commit/8f958bf354b0791510a8cdd3ca1a6addb8b5135e))

* Linear grating switch distance metric based on `rotation` ([`281acc4`](https://github.com/computational-psychology/stimupy/commit/281acc4e003b017083779402f6d75e165a2a852b))

* `waves.sine_linear`, `.square_linear` ([`f02940e`](https://github.com/computational-psychology/stimupy/commit/f02940e13e093246738588b2c4caab047ad38dc1))

* Add `stimupy.waves` ([`9ae3bfc`](https://github.com/computational-psychology/stimupy/commit/9ae3bfc3637e752987f235072f3eb1f8209119a7))

* Default intensities for `components.waves` ([`07e83e6`](https://github.com/computational-psychology/stimupy/commit/07e83e6b504bf3856f589e824e8bec83d1cd04e8))

* More complete output of `components.waves.sine()` ([`84485c0`](https://github.com/computational-psychology/stimupy/commit/84485c092f60a6790e688fe136d9676c1d233049))

* Docfix: docstring squarewave wrongly listed sinewave ([`b7cee3f`](https://github.com/computational-psychology/stimupy/commit/b7cee3f386be5667e48bb23a080498934fbcd020))

* Rename `grating_mask` instead of `mask` in `components.waves.sine()` ([`0ad53af`](https://github.com/computational-psychology/stimupy/commit/0ad53afb97f1f439d946aaa2ba2530045fe12c25))

* Create super-overview ([`3428970`](https://github.com/computational-psychology/stimupy/commit/3428970037398bd24fc1331611b0c4edcc61d298))

* Bugfix: Todorovic examples ([`0bc8350`](https://github.com/computational-psychology/stimupy/commit/0bc8350c1382cb75861e0e35b328c08e19a8a72d))

* Delbeouf as toplevel stimulus module ([`db64171`](https://github.com/computational-psychology/stimupy/commit/db64171c4380a36720556889d333fef6ccd7be5c))

* Mueller-Lyer as toplevel stimulus module ([`b287e95`](https://github.com/computational-psychology/stimupy/commit/b287e95c229075d9258fca8c75327e4b905440be))

* Ponzo as toplevel module ([`586300c`](https://github.com/computational-psychology/stimupy/commit/586300cbb3e64af4498a5e6f8ed0fc7166745dca))

* Hermann Grid as toplevel stimulus module ([`db4f007`](https://github.com/computational-psychology/stimupy/commit/db4f0070b3f3a3208caa5108f6f0c151f7397342))

* Start overview for `waves` ([`f79e535`](https://github.com/computational-psychology/stimupy/commit/f79e5354c62e34916702701f125bbec96997bf94))

* Default `rotation` for waves is 0.0, not None ([`b821bde`](https://github.com/computational-psychology/stimupy/commit/b821bdef2e66b60cea83966ba63606b2aa686ff1))

* Add `components.waves.square()`

Pretty much a carbon copy of `components.gratings.square_wave()`, but this is the &#34;generic&#34; function that is distance-metric agnostic (and thus deals in &#34;phases&#34; (rather than e.g. &#34;bars&#34;) ([`ca32001`](https://github.com/computational-psychology/stimupy/commit/ca3200186d253dd1ee87aa59f397a196d3af2979))

* Move `components.draw_sine_wave()` to `components.waves.sine()` ([`81a603c`](https://github.com/computational-psychology/stimupy/commit/81a603c59a69ca6856da661c0a86822edf3c5c59))

* Remove deprecated resolve_circular_params

and corresponding test

Closes #11 ([`54584f9`](https://github.com/computational-psychology/stimupy/commit/54584f97c7ec0621ec7d425b6c45efb717119c02))

* Plaids as toplevel stimulus module ([`293db27`](https://github.com/computational-psychology/stimupy/commit/293db27085f299a609880df54a90ebefc3402a9e))

* Benary as toplevel stimulus module ([`774cc1c`](https://github.com/computational-psychology/stimupy/commit/774cc1cc7691ed524ce55c48fab8929c270ea5c1))

* Cube as toplevel stimulus module ([`e87a5de`](https://github.com/computational-psychology/stimupy/commit/e87a5de346abc6ab793fec05be6e337b75aec960))

* Dungeon as toplevel stimulus module ([`c4449c6`](https://github.com/computational-psychology/stimupy/commit/c4449c650dabdf765efaff372dabb378789d8160))

* SBC as toplevel stimulus module ([`d44417a`](https://github.com/computational-psychology/stimupy/commit/d44417a72ba8aeffeccb539ffdf3f3ba53348acd))

* Todorovic as toplevel stimulus module ([`ce67d50`](https://github.com/computational-psychology/stimupy/commit/ce67d502a08054b84889a7192079792dd3d36700))

* Wedding Cake as toplevel stimulus module ([`01b4451`](https://github.com/computational-psychology/stimupy/commit/01b4451299cf86500b90a67c90ec248e9bc8baf7))

* White's as toplevel stimulus module ([`a59b28d`](https://github.com/computational-psychology/stimupy/commit/a59b28d1c855029a3d267465a32f9655854afbc6))

* Mondrians as toplevel stimulus

and collapsed `illusions/mondrians` with `components/mondrians` ([`c499a41`](https://github.com/computational-psychology/stimupy/commit/c499a413da54918d0937666e195bc0f5708fe9dd))

* Gabor as toplevel stimulus ([`e6f0197`](https://github.com/computational-psychology/stimupy/commit/e6f01976399bc5ab1e72d022329b6c261e5e3933))

* Merge pull request #6 from computational-psychology/lynn_issues

Added majority of demos and related bug-fixes ([`52108e5`](https://github.com/computational-psychology/stimupy/commit/52108e5631353f6db70544b54b103a35295d8b13))

* Also update launcher buttons branch ([`1ecedfb`](https://github.com/computational-psychology/stimupy/commit/1ecedfb1451b1b182968cb31b017195270db74c2))

* Update Binder links in demos

These should all point to the current `HEAD` (rather than `dev_docs` ([`65d8533`](https://github.com/computational-psychology/stimupy/commit/65d85334aec5af21fc96a19c0e998728d5dafa7a))

* Merge branch `main` into lynn_issues ([`258bd0c`](https://github.com/computational-psychology/stimupy/commit/258bd0c81da17ceb175c1da51ac111f8b82666ff))

* fixed bugs in part of illusions gratings; and started gratings-demo ([`5b9d48d`](https://github.com/computational-psychology/stimupy/commit/5b9d48dae1f40df2c5c385e62b81313a12483196))

* fixed mask-variable-name in circular demo ([`e248664`](https://github.com/computational-psychology/stimupy/commit/e2486645306a5e8ee500e6080275c7bd64a6bddf))

* updated wedding_cake; added limits and renamed variable ([`feb695d`](https://github.com/computational-psychology/stimupy/commit/feb695d8b89576fe25b640ec0cef475751269ce2))

* Merge pull request #4 from computational-psychology/dev_docs

Documentation: API reference, demos, README ([`0b3004f`](https://github.com/computational-psychology/stimupy/commit/0b3004f9bdfae68ecb0c1bec582caf277daf5232))

* Autoformat ([`006abd0`](https://github.com/computational-psychology/stimupy/commit/006abd0cae4db6159c1f488f935e0a459a9aaa12))

* Update `dev_docs` with base-branch `main` ([`371eb86`](https://github.com/computational-psychology/stimupy/commit/371eb86e6ffa0916fb4b0aaf5a5e18244cc6a050))

* autoformatting ([`364913d`](https://github.com/computational-psychology/stimupy/commit/364913d45a6e30c8e568f15fe2645e3d8e121f0e))

* updated RHS2007-json because of improvement in corrugated mondrians ([`6865fb7`](https://github.com/computational-psychology/stimupy/commit/6865fb71be13d1501bf9063b228bc47cd463d0a8))

* updated paper scripts to pass tests again (exception corrugated mondrians) ([`3e3fa64`](https://github.com/computational-psychology/stimupy/commit/3e3fa64cc1e820313f8eaf985c419b25a251ed77))

* Merge pull request #5 from computational-psychology/dev_dependencies

Dev: simplify installing dev environments ([`402e5e3`](https://github.com/computational-psychology/stimupy/commit/402e5e3981f333a63663a33d72fa5624e313077d))

* added a bunch of demos ([`f387bb9`](https://github.com/computational-psychology/stimupy/commit/f387bb94b8ab64229da9e67662287c5458c36918))

* fixed small bug in two-sided mueller lyer ([`a378ada`](https://github.com/computational-psychology/stimupy/commit/a378ada56aab66a9eb86ee6e7b15b5bae86f086e))

* fixed mondrians ([`65c290b`](https://github.com/computational-psychology/stimupy/commit/65c290b079ceb5026f67c4fa1695fa3bf9829eca))

* updated and unbugged frame-illusions ([`e91320a`](https://github.com/computational-psychology/stimupy/commit/e91320a782fdbd1c35de69c9a16e00f60113fe42))

* added target masks to delboeuf ([`f45221b`](https://github.com/computational-psychology/stimupy/commit/f45221bffbcee454340f12c7e58ae726bef924ca))

* simplified cubes to fix bugs ([`5d92cef`](https://github.com/computational-psychology/stimupy/commit/5d92cef2fafc131adb517affbe2252b6e22e6a8e))

* improved errors; added phase shift consistently ([`fc4a546`](https://github.com/computational-psychology/stimupy/commit/fc4a5460b04c09f2c5115b93493f832c44bc0abf))

* fixed bugs in checkerboards and added round_phase_width consistently ([`012d6bd`](https://github.com/computational-psychology/stimupy/commit/012d6bd58eed120cbc36f26189802b48004bfbec))

* fixed bugs and improved errors in benarys ([`925abec`](https://github.com/computational-psychology/stimupy/commit/925abec1da7d14d4dad25298f8ebfc8cb37ddef4))

* fixed problems and errorrs of pinwheel illusion ([`2d950ee`](https://github.com/computational-psychology/stimupy/commit/2d950eec02bfae1007335c9dbb2969bd643c8559))

* Bugfix: __all__ in stimupy.components should be list of str ([`b253954`](https://github.com/computational-psychology/stimupy/commit/b25395410a335902e1bb38bcf14cd7a770893696))

* Merge remote-tracking branch `github-public/main` into dev_docs ([`ffea283`](https://github.com/computational-psychology/stimupy/commit/ffea283d3298a55426b7a6bbc4de087a2b3c3e6d))

* Docs: define public API for components

Export only the entries in __all__ ([`fbf19b4`](https://github.com/computational-psychology/stimupy/commit/fbf19b439f986f5ed5def9f7839cc45d32b260b3))

* Docs: headings in docstrings ([`398e492`](https://github.com/computational-psychology/stimupy/commit/398e492977e2f32897d348e59917a94eaf9ee988))

* Docs: cleanup module-level docstring noises ([`e78bb11`](https://github.com/computational-psychology/stimupy/commit/e78bb11f89ef93e28b9ce9f603f13dd29676b504))

* Docs: Fix and unify toplines in docstrings ([`cdb7ebb`](https://github.com/computational-psychology/stimupy/commit/cdb7ebbd43aad64088842f6144b034e63363918a))

* Docs: bugfix RHS2007.todorovic_out docstring ([`ebf1cde`](https://github.com/computational-psychology/stimupy/commit/ebf1cde1092ccdd17c1586f1bd3e8dbf115195c3))

* Docs: Fix references in docstrings ([`312ddec`](https://github.com/computational-psychology/stimupy/commit/312ddeccbff554b76a8cb84b5ac559032c9e466e))

* Update requirements.txt's ([`3d3a457`](https://github.com/computational-psychology/stimupy/commit/3d3a4578c95c114f0ef1b8521d11fbf48d811369))

* Docs-dependencies specified in pyproject.toml

Can install using `pip install -e &#34;.[docs]&#34;` ([`bafb8f7`](https://github.com/computational-psychology/stimupy/commit/bafb8f72add1b4bb021aaea4d84ca07bbab67a70))

* Dev-dependencies specified in pyproject.toml

Can install using `pip install -e &#34;.[dev]&#34;` ([`5528cad`](https://github.com/computational-psychology/stimupy/commit/5528cad2c7bf99693d4af234ccacfb441e3d595a))

* pyproject.toml specify version earlier ([`ffe6c99`](https://github.com/computational-psychology/stimupy/commit/ffe6c9916c29df4d2ba5aced58014a1327e90aa4))

* Merge pull request #3 from computational-psychology/lynn_issues

Enhancements, bugfixes, cleanup, by Lynn ([`3288218`](https://github.com/computational-psychology/stimupy/commit/3288218e4da24006d26c219044920ccecc9dffe8))

* ran auto-formatting ([`d8578c0`](https://github.com/computational-psychology/stimupy/commit/d8578c092f29c964b198268a73ccc76e79d517b0))

* added circles (lines and shapes) ([`6f82203`](https://github.com/computational-psychology/stimupy/commit/6f8220329941bd0be106c9906e88fb9a795b7b77))

* Binder link demo links to lab interface, not raw notebook

Otherwise it gets rendered as plain markdown ([`d4ec3cd`](https://github.com/computational-psychology/stimupy/commit/d4ec3cd44058d117af2b8cc7e0c74204b61ee7af))

* ignore period argument for oblique gratings ([`956abd7`](https://github.com/computational-psychology/stimupy/commit/956abd78c41391296f77bb4e73119a2cb2246739))

* fixed that oriented gaussians and mask were rotating differently ([`f0c5a50`](https://github.com/computational-psychology/stimupy/commit/f0c5a5013242e8a284ff08599fc800d81fb85f57))

* fine-tuned frames ([`76fa262`](https://github.com/computational-psychology/stimupy/commit/76fa2625362e5fdd9608bdef149faf408c366d69))

* Update README ([`3a3302d`](https://github.com/computational-psychology/stimupy/commit/3a3302d3da7b070873bd05ea4e695cd6f44ecca5))

* Add documentation badge to README ([`8ab2760`](https://github.com/computational-psychology/stimupy/commit/8ab276099c017ff79d0eadacaab31c02e3cf64e2))

* made cornsweets rotatable ([`af0a83a`](https://github.com/computational-psychology/stimupy/commit/af0a83a292200c28bf361d632e2ff29089bde5b6))

* Revert f415243

No need to enable extensions on Binder ([`fe43dd8`](https://github.com/computational-psychology/stimupy/commit/fe43dd8f3628d0a39a1211268ee1dc22bfc151d9))

* Specify optional dev-dependencies for docs in pyproject.toml

Can install using `pip install -e &#34;.[docs]&#34;` ([`179f292`](https://github.com/computational-psychology/stimupy/commit/179f2928a4b7c57373ae29ac33e9dd1140b47793))

* fixed use of intensity values in gaussian edge; added gaussian mask ([`6ba4dab`](https://github.com/computational-psychology/stimupy/commit/6ba4dab8270937e3e75a49d6d94446dbc67f5f9c))

* added argument to ellipse to allow ellipse to reach beyond image size - used in gaussian mask ([`87ecc32`](https://github.com/computational-psychology/stimupy/commit/87ecc32eaab1356ad00636fe8b3814de70ad17aa))

* Add MystNB to requirements to enable to Binder ([`111b3d1`](https://github.com/computational-psychology/stimupy/commit/111b3d1fcd32dec07eaddf1e1ae41044b128a6d7))

* Override default viewer on Binder to open MySTs as JupyText Notebooks ([`f52bf29`](https://github.com/computational-psychology/stimupy/commit/f52bf29786af6c3e82c12e169a96d63055c8efd3))

* Install &amp; enable JupyText on Binder ([`f415243`](https://github.com/computational-psychology/stimupy/commit/f415243a3814a142c87a60fe8968ac81e28cbe7e))

* Use JupyterLab interface on Binder ([`eb3d718`](https://github.com/computational-psychology/stimupy/commit/eb3d7185c6e9be3c703b0a41b2dc71232ca141cb))

* fixed bug - order argument was always 0 in bessel ([`3cc88a1`](https://github.com/computational-psychology/stimupy/commit/3cc88a101fc82907e9c82f622776bcb5d52e832d))

* removed period arg from circular gratings ([`7366271`](https://github.com/computational-psychology/stimupy/commit/7366271308502618ecff5d3c78e657cd169edcbe))

* fixed missing variable in overview ([`202ac09`](https://github.com/computational-psychology/stimupy/commit/202ac093a2701e3a02c6bf3ed37c4f840874bfde))

* renamed carney-files to modelfest ([`a7b8258`](https://github.com/computational-psychology/stimupy/commit/a7b8258eb29fc632eb7c24d9675c46112f337699))

* fixed rings, discs, and pinwheel ([`6505d0e`](https://github.com/computational-psychology/stimupy/commit/6505d0e8328744abf4fea64b51e7b565799a13aa))

* merge conflicts part 2 ([`27341ec`](https://github.com/computational-psychology/stimupy/commit/27341ecce2afd9a18f9da515a5f0bb325d52472c))

* resolved merge conflicts ([`0f4c542`](https://github.com/computational-psychology/stimupy/commit/0f4c5424b309e35971d5da78ebe347ddc407f0b3))

* updated and fixed all grating functions in components, and functions using them ([`62b081a`](https://github.com/computational-psychology/stimupy/commit/62b081aedadc9235c753f0a265c774af660c298b))

* fixed bug in component grating masks; added clipping to circulars and frames gratings ([`3b7e119`](https://github.com/computational-psychology/stimupy/commit/3b7e11968f4e7922c0898bfe2b4c49e22833456e))

* Fall back to earlier version of jupyter-book ([`0ecefc3`](https://github.com/computational-psychology/stimupy/commit/0ecefc336cb85d8fe0cfafdf3c6d350ba950bf3a))

* Merge pull request #2 from computational-psychology/dev_test_CI

Enable Continuous Integration (CI) ([`a5203fe`](https://github.com/computational-psychology/stimupy/commit/a5203fe9c6aa03c15510f888960e120351f720f8))

* Run linting only on main branch, and pull-requests ([`4898a50`](https://github.com/computational-psychology/stimupy/commit/4898a50b160327fdd9ffb6fda48d2ed995d799a0))

* More explicit handling of TooManyUnknowns (vs. other resolution errors)

Fixes some flake8 warnings ([`5f437bb`](https://github.com/computational-psychology/stimupy/commit/5f437bb20bdd05f570c677d88d3371512e5ad62e))

* Pyupgrades: remove `r` from open(json) ([`c2bfe08`](https://github.com/computational-psychology/stimupy/commit/c2bfe0886ad9e77b3201b5e2b0d5a6234622ba69))

* Pyupgrade as pre-commit hook

Upgrades syntax to newer forms ([`34cecaf`](https://github.com/computational-psychology/stimupy/commit/34cecaf3af2985245b56962cf98f96f4796284b8))

* Black'en ([`2af2109`](https://github.com/computational-psychology/stimupy/commit/2af21096051a339f649e6e5410988086e3707907))

* Black: also format Jupyter Notebooks ([`f97700b`](https://github.com/computational-psychology/stimupy/commit/f97700bf84310fab12b8dbc5365d7d22552652a3))

* flake8: don't check for naming, tests, ignore some (import) errors in inits ([`2727279`](https://github.com/computational-psychology/stimupy/commit/272727919644a49df29663222adfaea76659a9b0))

* Add GHA workflow for linting + formatting ([`16ccb5d`](https://github.com/computational-psychology/stimupy/commit/16ccb5d6c3e12c9a929ed9afde35fa412efd6077))

* Include pre-commit hook in Nox ([`1b711f6`](https://github.com/computational-psychology/stimupy/commit/1b711f685ab56045f40d84f95ac2b26b7cae3de1))

* Setup formatters as pre-commit hook

(to use: pip install pre-commit; pre-commit install) ([`eae9d61`](https://github.com/computational-psychology/stimupy/commit/eae9d611cdff1455b525b6ece412a70fc0224ff0))

* Add configuration for formatters: Black, isort ([`f9ac5e5`](https://github.com/computational-psychology/stimupy/commit/f9ac5e59bce6ed341d0f31ec73b0614298813538))

* Drop Windows support (for now)

Was failing on masks (but not images) of paper stimuli ([`e571c58`](https://github.com/computational-psychology/stimupy/commit/e571c58ebd2b4eed7d0ad9c342bc9b3bf1452488))

* Don't &#34;fail fast&#34;, i.e., complete all platforms, even if earlier fails ([`573cdc3`](https://github.com/computational-psychology/stimupy/commit/573cdc321b7fabb0ba2b743e2a8e32061c7b1a7c))

* Run tests on multiple platforms ([`272bcab`](https://github.com/computational-psychology/stimupy/commit/272bcab1820f5ec26dca8bd36b929400e494008a))

* Setup to run tests on pull request as well ([`aa15102`](https://github.com/computational-psychology/stimupy/commit/aa15102d473eb9c76a625f5523bee7549411088c))

* Reorganize GHA yml a bit

- Upgrade pip, setuptools before installing deps
- Run nox through pipx ([`b09d7c0`](https://github.com/computational-psychology/stimupy/commit/b09d7c038101e3d0a00bd3d9e75f24cb5e3c4e15))

* Add badges for tests, Python versions ([`274b4c6`](https://github.com/computational-psychology/stimupy/commit/274b4c652248375b243f297e8ce465d73ba3894c))

* Test for Python 3.8 - 3.11 ([`acc007e`](https://github.com/computational-psychology/stimupy/commit/acc007e21ee4ed9350ca161b220216815b0573a8))

* Run Nox on GitHub Actions ([`9c94b91`](https://github.com/computational-psychology/stimupy/commit/9c94b914292040dcc9071807d04c80c7f4c712c9))

* Noxfile for automating builds through Nox ([`87e4254`](https://github.com/computational-psychology/stimupy/commit/87e4254433bb7559ae9f868557ec6c96e954c90e))

* Update ground-truths ([`9f01e75`](https://github.com/computational-psychology/stimupy/commit/9f01e7532880c724466bcf5de02acb373df2e3fa))

* Round to 8 digits before hashing ([`16e1079`](https://github.com/computational-psychology/stimupy/commit/16e10791985e26ed9c93c3ea343fca9596b65fe0))

* made order of intensity_vals in square-waves and sine-waves consistent, updated functions and papers using the code ([`1c2ecd1`](https://github.com/computational-psychology/stimupy/commit/1c2ecd16e4dbbb92ec24022aa950aad059d11534))

* added new frames and circular components to overview ([`d15d172`](https://github.com/computational-psychology/stimupy/commit/d15d1724bdf8b8187aeea7962e100f9616d9ccd3))

* made draw_sine_wave separate; added frames and circulars sine-wave and square-wave; corrected bug in circular gratings ([`9d7fb21`](https://github.com/computational-psychology/stimupy/commit/9d7fb218a4dae958ed7a86a2f146ed4856288646))

* GitHub Actions configuration ([`24dcd15`](https://github.com/computational-psychology/stimupy/commit/24dcd15b0809fbf684eabe889b6fa6f9350f15fa))

* Requirements for installing pytest ([`2de2a32`](https://github.com/computational-psychology/stimupy/commit/2de2a32b955ca4d7d1fa2a30e45278f1e44a25ca))

* Merge branch `feat_demos` into dev_docs ([`09cc5b7`](https://github.com/computational-psychology/stimupy/commit/09cc5b7eac9ae7b3013c9812201cffc52748d00f))

* Add demo basic shapes ([`a1e6234`](https://github.com/computational-psychology/stimupy/commit/a1e6234ca0d9980a743cf8146a1e59b460b00256))

* Use separate templates for different modules

Components, illusions have demos -- utils &amp; papers do not ([`44b7814`](https://github.com/computational-psychology/stimupy/commit/44b781400cc1f45405a482fe8a1534a18e9e63e5))

* Merge branch `feat_API` into dev_docs ([`27faa20`](https://github.com/computational-psychology/stimupy/commit/27faa209aee55e79492d61bb1dd451031fbe0f2d))

* Use custom template for API reference

This requires the config `templates_path` to be set, in order to find the template(s). Unfortunately, this seems to overwrite where the theme cannot find its templates anymore. We can get around this for now by fixing some older versions of sphinx-book-theme and pydata-sphinx-theme ([`63bdb5b`](https://github.com/computational-psychology/stimupy/commit/63bdb5b3a3d2e9cf4bc40e3bfc0149bc673c4565))

* Autoinclude source-code in build HTMLs (and link from API reference) ([`aa59fbd`](https://github.com/computational-psychology/stimupy/commit/aa59fbd47da3883c3c8e5d5b44e6254ce2862de6))

* Autodoc should respect `__all__`-attributes ([`0d2c040`](https://github.com/computational-psychology/stimupy/commit/0d2c040daaf0a3c53a354f92bb37079e74cb455c))

* Also document imported members

e.g., shapes.disc (imported from circular.disc) ([`129d298`](https://github.com/computational-psychology/stimupy/commit/129d298e11fcc28454d52c3195d667dcf194b27c))

* Autodocument `members` ([`7b87fe7`](https://github.com/computational-psychology/stimupy/commit/7b87fe74b7a9e2956237eab413cf40d88c584ba4))

* Comment-out autosummary_generate

This option controls whether `autosummary` generates the stub `.rst`-files based on the `autosummary::` directive.
This is `true` by default. ([`c90b44a`](https://github.com/computational-psychology/stimupy/commit/c90b44aef4f997243130393525bdb35165ca8528))

* Recognize NumPy docstrings

`napoleon` Sphinx extension can auto-translate NumPy (and Google) style docstrings to standard `autodoc`-docstrings ([`dbda8cc`](https://github.com/computational-psychology/stimupy/commit/dbda8ccd248b0bed0c1dcfd65905bd40ee3912f5))

* Ignore generate _api docs ([`5b9d444`](https://github.com/computational-psychology/stimupy/commit/5b9d444148c6e1eae0e0110a235af49fc815dd13))

* Autosummary generates documentation for modules

As well as &#34;summary&#34; tables of members ([`1285041`](https://github.com/computational-psychology/stimupy/commit/12850418d7254a1971e70af81c13da0e3e63361b))

* Landing page for API reference


Link to API ref from index ([`5f2b51a`](https://github.com/computational-psychology/stimupy/commit/5f2b51ab50a5920d95446d7583bf7eeb526bb19d))

* Suppress warning about `toctree directive not expected when using etoc` ([`5a31ec6`](https://github.com/computational-psychology/stimupy/commit/5a31ec6a013c9ef0fb9314cbb8c99a4d2db80807))

* Build RTD docs using python3.11 ([`6cd9b62`](https://github.com/computational-psychology/stimupy/commit/6cd9b62b2263a01d76abf45b50738e9c3affc30f))

* Use intersphinx on installation page ([`43057ea`](https://github.com/computational-psychology/stimupy/commit/43057ea842fa1d590d0fbb256e62b0765f6c39c5))

* Update installation pip from GitHub

Use the `zipball` method, to avoid problems if a user doesn't have git installed ([`ad85f81`](https://github.com/computational-psychology/stimupy/commit/ad85f814839d285ada06aabdd8dc90f6844d53bf))

* Configure intersphinx ([`d687715`](https://github.com/computational-psychology/stimupy/commit/d687715336427d82030dbe6fd4190c3b47d36803))

* fixed bug in domijan2015-rings; raising error for odd ppds because stimulus behavior is not fully robust ([`48c5721`](https://github.com/computational-psychology/stimupy/commit/48c572121d1c6d3f1ef4cfbb3d4d25aaced3bd62))

* reduced use of scipy to utils ([`4e483ed`](https://github.com/computational-psychology/stimupy/commit/4e483ed7f1a81fc9228f6d49a14a33dcbe283d10))

* changed function behind grating-components ([`edfd985`](https://github.com/computational-psychology/stimupy/commit/edfd985e01c48216d91b05e3f089bc95eed31d74))

* fixed small bug for small colormap ([`d6b4867`](https://github.com/computational-psychology/stimupy/commit/d6b4867a3ffe5b8a3df3034e213cf5d4b4230367))

* separated and added contrast conversion functions for arrays and dicts ([`770bcfd`](https://github.com/computational-psychology/stimupy/commit/770bcfdc8cb7b15f0f07c1306693f4acfbe7c327))

* Merge branch `feat_Binder` into dev_docs ([`21341e2`](https://github.com/computational-psychology/stimupy/commit/21341e22d30342a52cb7cafb0d57b22ec681847f))

* Add a binder `postBuild` file

Necessary to install `stimupy` itself on Binder after building Docker image before opening Notebook(s) ([`5c294d6`](https://github.com/computational-psychology/stimupy/commit/5c294d6f9d0acd9f3dc2bbc97e75765bf698ae78))

* Add a general requirements.txt

Include docs/requirements.txt ([`fbf6b6c`](https://github.com/computational-psychology/stimupy/commit/fbf6b6c6776fcb23c064ba22ae444a74e283577e))

* For now, use `dev_docs` branch for Binder ([`72b6251`](https://github.com/computational-psychology/stimupy/commit/72b6251e9d338d999f5151364b1715d664347689))

* Add launch buttons and config for Binder ([`864e836`](https://github.com/computational-psychology/stimupy/commit/864e8364acd8bda3632e6bc4f40370083d32e829))

* plotting functions does not throw an error if it cannot find the mask, but just skips the mask ([`d4eff76`](https://github.com/computational-psychology/stimupy/commit/d4eff76fec189e60a980b67f3732767c0e452d44))

* fixed bug of switched extent coords if no extent is passed ([`9e0e519`](https://github.com/computational-psychology/stimupy/commit/9e0e51947495bda9866f868066ccd48da98d1396))

* updated reference in bindmann2004.py ([`ba09e06`](https://github.com/computational-psychology/stimupy/commit/ba09e06ba77ac8605647c573463f9a5280e66916))

* added papers bindmann2004 ([`ae39e9b`](https://github.com/computational-psychology/stimupy/commit/ae39e9b41907c090a8be370ad7695ec54e18deb3))

* uncommented two_sided rings ([`b502b37`](https://github.com/computational-psychology/stimupy/commit/b502b37a1b4f9629a03f25b324b2a4f8d1e322a0))

* fixed bug and added pad_masks when padding dicts ([`c0e8cec`](https://github.com/computational-psychology/stimupy/commit/c0e8cecf7711af234ba1174d2c20665881ca35ed))

* fixed bug that height and width of extent were switched ([`1f217f3`](https://github.com/computational-psychology/stimupy/commit/1f217f33c9195f42276ea6e68be85f59e0bcd3c2))

* corrected docstrings - mask to target_mask ([`20de701`](https://github.com/computational-psychology/stimupy/commit/20de70167f4249eede3e00eb220e8a531ee71c65))

* added utils to get all function argument names, and to strip dictionary from all keys which are not function argument names ([`f1951a8`](https://github.com/computational-psychology/stimupy/commit/f1951a84a71583b9be512ef19889a80497c585d8))

* corrected resolution docstrings ([`4b45d56`](https://github.com/computational-psychology/stimupy/commit/4b45d561b3b7228cacd5c428c04a98d29bcd1606))

* reorganized functions; added resolve_dict and valid_dict ([`983c11d`](https://github.com/computational-psychology/stimupy/commit/983c11d4f7e869f74f8586c461d31ae544a839b6))

* added all missing docstrings, re-organized utils, replaced degrees_to_pixels by resolution-funcs ([`7e37afd`](https://github.com/computational-psychology/stimupy/commit/7e37afd65c5484722e4bbbe6c557013a76cd41d6))

* fixed bug that two_sided dotted sbcs did not contain correct shape and visual_size ([`16fe40b`](https://github.com/computational-psychology/stimupy/commit/16fe40b05df8156c7151de5fce26b81f389608b5))

* fixed bug that parallelogram and ellipse would not contain correct size params in output dict ([`92acc3c`](https://github.com/computational-psychology/stimupy/commit/92acc3cb63d4a33c40cec73f5cb27a1d633137aa))

* made filters functions (currently only bandpass) more consistent with stimupy workflows ([`33e0c02`](https://github.com/computational-psychology/stimupy/commit/33e0c027fbe8862f2be2b641cf8d1d0413bc6407))

* removed oriented noise for now ([`0fbb166`](https://github.com/computational-psychology/stimupy/commit/0fbb166672eec7201e5100a264007aca4ef42c07))

* renamed carney1999 into modelfest ([`154cb32`](https://github.com/computational-psychology/stimupy/commit/154cb3202a981aeff5ed360e3e34797a4568cdb1))

* updated carney1999.json ([`9a65fc1`](https://github.com/computational-psychology/stimupy/commit/9a65fc13d3206596180202046c2b5543f7ff3609))

* corrected keys for shape and visual_size for stimuli that involved stacking or padding ([`4750caf`](https://github.com/computational-psychology/stimupy/commit/4750cafc6a8326d9b56c9338f3dd55e74dd9addc))

* plotting functions take argument extent_keys for changing extent param of plots ([`dd38b35`](https://github.com/computational-psychology/stimupy/commit/dd38b3546380c231e2eb02d132ad4716b6ed7256))

* pad_dict utils now also update visual_size and shape keys ([`86bc84a`](https://github.com/computational-psychology/stimupy/commit/86bc84a06eaa1e61566852e9718d13f5a861c32d))

* closes #94; fixed all intensity ranges for modelfest. our modelfest now perfectly recreates original in all cases but checkerboard ([`99578b2`](https://github.com/computational-psychology/stimupy/commit/99578b230a047d56463105bcf9a41414fb3323d8))

* now ignoring folder with original modelfest for testing ([`25fa0b6`](https://github.com/computational-psychology/stimupy/commit/25fa0b6e6739367511885a00c73dfbe8d80b149f))

* Merge pull request #1 from computational-psychology/dev_docs

Publish (draft) documentation ([`9e37617`](https://github.com/computational-psychology/stimupy/commit/9e3761793c3f2fbb1583662a73188486108a3058))

* Some style updates to docs ([`18ddcea`](https://github.com/computational-psychology/stimupy/commit/18ddcea69282befa071d2b511439ef0968effc51))

* Merge branch `feat_tutorial` into dev_docs ([`81cb64d`](https://github.com/computational-psychology/stimupy/commit/81cb64dc057227f8e0a54a687f9689f3cacc5f46))

* Merge branch `feat_installing` into dev_docs ([`6d1cbab`](https://github.com/computational-psychology/stimupy/commit/6d1cbaba0804dee105b6dff0ae2e8946a44b1dd4))

* Update dependencies ([`78830db`](https://github.com/computational-psychology/stimupy/commit/78830db3edd6a8da5a5658eb7e2770b04828c31a))

* Merge branch `feat_JB` into dev_docs ([`2fa81ea`](https://github.com/computational-psychology/stimupy/commit/2fa81ea9607fa2dc92648b4b330194ac945c3626))

* Basic installation instructions ([`84f6b75`](https://github.com/computational-psychology/stimupy/commit/84f6b75faa93d4b6ba4ff2ecc9a052181a70e71b))

* Tutorial: replicate paper stimulus ([`31453b8`](https://github.com/computational-psychology/stimupy/commit/31453b8b0179fe0680ec7625cce75d7f37f6e17f))

* Tutorial: illusions ([`c394253`](https://github.com/computational-psychology/stimupy/commit/c39425304d401ac3b8f7b2cadaa39d3439de2d48))

* Tutorial for creating a basic stimulus from components ([`2122330`](https://github.com/computational-psychology/stimupy/commit/2122330a90f0231095de6055e58814deb636ec79))

* Configure ReadTheDocs using JupyterBook ([`9610f43`](https://github.com/computational-psychology/stimupy/commit/9610f436b81e39b2973a0b4d327410680d091e4b))

* Basic skeleton for documentation ([`e699511`](https://github.com/computational-psychology/stimupy/commit/e69951145cb10e7c92d69568622cecb9bf5a84a5))

* Merge branch `dev` into main ([`cfd6047`](https://github.com/computational-psychology/stimupy/commit/cfd604767d636ac52be8aa74d7adadfe0f0a3b94))

* Merge branch `feat_packaging` into dev ([`8e36371`](https://github.com/computational-psychology/stimupy/commit/8e3637138a7192d3f9a6bb02e10796ccdc0b2533))

* Modern packaging setup

Use only pyproject.toml

Mark version in stimupy.__version__ ([`23b75ba`](https://github.com/computational-psychology/stimupy/commit/23b75ba446c8867036aae97047abd053aa9952fc))

* Merge branch `dev_rebrand` into dev ([`e124d3d`](https://github.com/computational-psychology/stimupy/commit/e124d3d99bc22ffa8f5a89d0ee2748234efc43a9))

* Cleanup imports ([`ffa8dd3`](https://github.com/computational-psychology/stimupy/commit/ffa8dd3927376394b7490a2dbea606bda7b151a8))

* Basic update README ([`d5b1a96`](https://github.com/computational-psychology/stimupy/commit/d5b1a96b9997d69bfbee71fa3480bf380e2116c9))

* Also update manuscript ([`0b48122`](https://github.com/computational-psychology/stimupy/commit/0b48122ade527b2e59fbad11ce98a70d1729a119))

* Update notebooks ([`f12d1f4`](https://github.com/computational-psychology/stimupy/commit/f12d1f48ca74eb4fcfe3e67cab8948edb46f4ba8))

* Update docstrings ([`6a420b0`](https://github.com/computational-psychology/stimupy/commit/6a420b03f96d0f691feea962a16f2ca858e4669b))

* Rename dir to `stimupy` ([`e78fa9c`](https://github.com/computational-psychology/stimupy/commit/e78fa9c633f9d407668384f5addb5ac2a03af638))

* Remove some floating files ([`ba3f5de`](https://github.com/computational-psychology/stimupy/commit/ba3f5de483f251895bcdfb90714f53c3b687cc79))

* Test overviews ([`cd3faf4`](https://github.com/computational-psychology/stimupy/commit/cd3faf4b6458ac06e3ae1166387af6fbf67c488d))

* Separate generating overview from plotting overview ([`99d8f0b`](https://github.com/computational-psychology/stimupy/commit/99d8f0b491506f924f4290ecf248fc1fae2fd450))

* Minor bugfix ([`176276b`](https://github.com/computational-psychology/stimupy/commit/176276b43941961a036e4a19cfc1997731300938))

* plotting function now creates colormaps for masks with many elements ([`741b190`](https://github.com/computational-psychology/stimupy/commit/741b190f089d45174fabee2ef92b5cb468beb750))

* closes #120; moved overviews to inits ([`9a65592`](https://github.com/computational-psychology/stimupy/commit/9a655922b07e6f08100fc34770952131a509b700))

* changed handling of colors for masks with many indices ([`a162d54`](https://github.com/computational-psychology/stimupy/commit/a162d548ed2280db861dfed628c117e4d7b73a25))

* closes #118; circular grating now outputs correct non-int number of rings ([`de916f9`](https://github.com/computational-psychology/stimupy/commit/de916f97577645c20238f215a36dc56d6b001849))

* specify which `mask` to plot

Closes #109 ([`223777a`](https://github.com/computational-psychology/stimupy/commit/223777a22ebc09260d8b1897f2152945793bc3de))

* closes #119; added more instructive errors if relevant function arguments are None ([`7376393`](https://github.com/computational-psychology/stimupy/commit/7376393769c8089397cc6189a0f82d5a5852298a))

* created components overview, fixed some bugs ([`b5280a9`](https://github.com/computational-psychology/stimupy/commit/b5280a9dbc6e1f938baff7f431b8951c7240581e))

* removed contrast from input variables ([`16da7ad`](https://github.com/computational-psychology/stimupy/commit/16da7add80aef2a13f534b67973e68b2369f868e))

* removed checkerboard test ([`294b4f4`](https://github.com/computational-psychology/stimupy/commit/294b4f4593d96f3b3e8d4e057c1567a59f182d4d))

* updated non-paper test cases ([`e23454b`](https://github.com/computational-psychology/stimupy/commit/e23454b82eede2aa153add3209f0457d326485cf))

* closes #112; added utility functions for two-sided stims ([`ee739f4`](https://github.com/computational-psychology/stimupy/commit/ee739f4689a0c5dc6727e8c2270227f6bab670a7))

* fixed bug that frames_grating could only be square image ([`b0c3f39`](https://github.com/computational-psychology/stimupy/commit/b0c3f395a1bc280a7adc006be2d7b341ea283e11))

* temporary fix for circular_grating if frequency does not perfectly work out ([`9484c9f`](https://github.com/computational-psychology/stimupy/commit/9484c9f6b3e4825fe2a367e44397a110d1472e1d))

* fixed bug that circular gratings were always squared images ([`443085f`](https://github.com/computational-psychology/stimupy/commit/443085f28099563a3980ea30f7b0d00ea4a4d9a5))

* corrected shape arguments in two-sided-sbc ([`c89365c`](https://github.com/computational-psychology/stimupy/commit/c89365cfab0d8329758e350fe946bb0b6a89298b))

* corrected target positions argument in two-sided-sbc ([`5eb3400`](https://github.com/computational-psychology/stimupy/commit/5eb34008e1acd6f3fef5f7886ff82c70fa71fd90))

* added two-sided sbc ([`4fc3d16`](https://github.com/computational-psychology/stimupy/commit/4fc3d1606308c319078faae5b425c9f68d9865c4))

* renamed checkerboard targets to target_indices ([`dd3b354`](https://github.com/computational-psychology/stimupy/commit/dd3b354bbd2ab76761741221b944f33f4e90070a))

* closes #102; renaming of modules and functions ([`d75c5d5`](https://github.com/computational-psychology/stimupy/commit/d75c5d5514f3aaf2271030458f7fcca279b6dc20))

* updated naming and overview with ponzo and mueller_lyer ([`b4415f0`](https://github.com/computational-psychology/stimupy/commit/b4415f0aa3e257ea763863b36bd51eab671f9431))

* closes #84; added mueller_lyer ([`0f86a01`](https://github.com/computational-psychology/stimupy/commit/0f86a01e5ca470516e2c0c1a4ca26f5e2e0264bc))

* updated gaussian docstring ([`0560b07`](https://github.com/computational-psychology/stimupy/commit/0560b0780d3eb38775d152edc90e41bb5b0656d9))

* fixed bug, added origin to gaussian-mask ([`4c4e14f`](https://github.com/computational-psychology/stimupy/commit/4c4e14fe61b1f1f7e828955811e147fefb995ec8))

* closes #100; added masks to Gaussians, also in Gabors and plaids ([`1cfdfa2`](https://github.com/computational-psychology/stimupy/commit/1cfdfa2cb053b0494d14a6a58f32d72969a74d33))

* changed rotation behavior of ellipse ([`48ded6e`](https://github.com/computational-psychology/stimupy/commit/48ded6e66b88ccc74b752df7ad46ec1b9b947a5f))

* closes #101; added ellipse component ([`aca11f3`](https://github.com/computational-psychology/stimupy/commit/aca11f3c77d0b6a6c248b62a8f17d1dcf6706a23))

* closes #52; we now differentiate between target_masks and other masks ([`956b918`](https://github.com/computational-psychology/stimupy/commit/956b9181be13742d1315ed568b82261a10113754))

* closes #46; removed supersampling ([`980a01e`](https://github.com/computational-psychology/stimupy/commit/980a01e476134c03d0fbfdce576bf9d911a19b81))

* updated overview to new white-use ([`a97debc`](https://github.com/computational-psychology/stimupy/commit/a97debc7b4432045da94729f4121fd42a4be5f8f))

* closes #54, closes #65, closes #35; using new grating function in whites - this led to 1px-changes in RHS2007-howe and anderson ([`df751a5`](https://github.com/computational-psychology/stimupy/commit/df751a5a9ed2bd93a1784958fc350cc21b2d68dc))

* updated masked grating use in overview ([`7dc712b`](https://github.com/computational-psychology/stimupy/commit/7dc712b0cfa7816a46f457db652fb20ba2e6814e))

* closes #99; made all shapes rotatable, updated scripts and rhs2007 and white1981 for slight changes in parallelograms ([`6590b96`](https://github.com/computational-psychology/stimupy/commit/6590b96e81bbd0e6c73de0a2f160f81d95814cd8))

* removed old backup grating file ([`33350e3`](https://github.com/computational-psychology/stimupy/commit/33350e306e3cdb01288356f99d52d5ea539ba3b5))

* added an additional function for grating_induction_blur which blurs a square-wave grating ([`ea3f7d1`](https://github.com/computational-psychology/stimupy/commit/ea3f7d19879dc167870f1c22e99c4fdf96ce9fd2))

* closes #97; updated grating_induction everywhere to use sine-wave rather than blurring ([`70e9eba`](https://github.com/computational-psychology/stimupy/commit/70e9eba03433b4400d76b8c8023e1c049eea7bf1))

* closes #98; added grating illusions to overview ([`ff944aa`](https://github.com/computational-psychology/stimupy/commit/ff944aa517b5f1e677fe204abd09412d515928a3))

* added all grating functions to __all__ ([`b45c96b`](https://github.com/computational-psychology/stimupy/commit/b45c96b815c2a3a55b9b3651b0a63046a5dbc40a))

* by default, dont plot masks ([`ead7312`](https://github.com/computational-psychology/stimupy/commit/ead731232ec279cc72bd2125dadb066eb1a2c344))

* added test cases for white1981 and white1985 ([`5b8a22f`](https://github.com/computational-psychology/stimupy/commit/5b8a22f8aead5e02b003f078f9a0a7bdcb50d964))

* updated sizes in docstring and added warnings ([`c62fced`](https://github.com/computational-psychology/stimupy/commit/c62fcedf6a09b08302bb85ab1d576ec50304b563))

* updated target masks of counterphase illusion ([`af49d0c`](https://github.com/computational-psychology/stimupy/commit/af49d0c3a77c2454a7aebb313791c53e87bf7950))

* closes #96, closes #24; fixed grating illusions and added white1981 and white1985 ([`0b3e632`](https://github.com/computational-psychology/stimupy/commit/0b3e632c3475755e9709ba609a1e7364b17cbcbd))

* added rounding to avoid changes at floating-point precision ([`94118d8`](https://github.com/computational-psychology/stimupy/commit/94118d8fd72c1ebf76ea5c610ac9d6e20189d6c3))

* added rounding to avoid changes at floating-point precision ([`866d3d0`](https://github.com/computational-psychology/stimupy/commit/866d3d071e92e6ae7d8d73d390e2fbc57dc8a65d))

* closes #95, fixed bugs/inconsistent behavior in edge placement ([`d0f7f9b`](https://github.com/computational-psychology/stimupy/commit/d0f7f9bc4478a692347877443956e92713762dd2))

* rounding visual angle slightly changed carney1999-Gaborstrings and RHS2007-bullseye_thin for the better, recreating json ([`f51c71e`](https://github.com/computational-psychology/stimupy/commit/f51c71e657e5ae5f8f901ce512401e341fb55c2c))

* now flooring impossible visual angle ([`5a7c162`](https://github.com/computational-psychology/stimupy/commit/5a7c16264b1d66d1c44df31b01dea9b1033963db))

* added tests for modelfest and updated many component-masks for that; updated RHS-json with new bullseyes ([`992dbab`](https://github.com/computational-psychology/stimupy/commit/992dbab8030e80dc27ef5b56f91aa057195247b7))

* stacking dicts now by default increases mask_idx ([`90b2bcb`](https://github.com/computational-psychology/stimupy/commit/90b2bcb696e0ea697af6808bc5281aece97ee293))

* closes #90; added experimental data to murray2020, RHS2007 and carney1999 ([`5f32da3`](https://github.com/computational-psychology/stimupy/commit/5f32da3196e4471801f94858ed9ae548defb5dd7))

* closes #74; added optional shape arguments to dotted sbcs ([`828437e`](https://github.com/computational-psychology/stimupy/commit/828437e693bd7efe94f22d904026c5b5b108d976))

* closes #69; added general-purpose frames and bullseye to create domijan-stims ([`d7e2ccb`](https://github.com/computational-psychology/stimupy/commit/d7e2ccb2e272c7d27f50626bdffd85bd1d6a9d68))

* updated overview and some cleanup ([`9003db0`](https://github.com/computational-psychology/stimupy/commit/9003db00ca1e7bda29ccbac5ca9e2e71cdf57baa))

* corrected bug in dot sbcs ([`f9d8a6a`](https://github.com/computational-psychology/stimupy/commit/f9d8a6ac5dd3157b1ac9522332deb11ceab06bd2))

* corrected bug that mask_idx skips 1 in disc ([`a5241fe`](https://github.com/computational-psychology/stimupy/commit/a5241fe0355e9131251455ed79c4806476d4fabb))

* closes #82; added delbouef illusion ([`ac26631`](https://github.com/computational-psychology/stimupy/commit/ac266310c997f1378e3c4b282dddbe2f4b7f099f))

* corrected mistake in docstring ([`18382e0`](https://github.com/computational-psychology/stimupy/commit/18382e071ba0a78a1614247dc1d7bb22ce45de86))

* added documentation to ponzo ([`c4ec78a`](https://github.com/computational-psychology/stimupy/commit/c4ec78a40e9e1b8e341fef3ecba6c10fc6fb4928))

* added lines-circle ([`e739560`](https://github.com/computational-psychology/stimupy/commit/e739560bae418770a1dd4fda00ff0694b854327d))

* closes #86; added Ponzo illusion ([`83c7e15`](https://github.com/computational-psychology/stimupy/commit/83c7e152e066137d8132310af2f89e417a8d9bff))

* closes #77; implemented all spatial modelfest stims ([`1d1c183`](https://github.com/computational-psychology/stimupy/commit/1d1c1831ff3cbf76563c18375a94333f7ba57e59))

* closes #85; added lines and line-dipoles ([`238c405`](https://github.com/computational-psychology/stimupy/commit/238c405671634c789d1588a568468c0dd5c189d0))

* added documentation to plaids ([`45c9ea8`](https://github.com/computational-psychology/stimupy/commit/45c9ea84ecf747f213b6e0aa442510b99eab7aa2))

* closes #91; added plaids ([`aa01729`](https://github.com/computational-psychology/stimupy/commit/aa017295a74a3899682b30f8cb844fa67384d71b))

* fixed bug - moved edge shifting away from mask_elements ([`9596b5d`](https://github.com/computational-psychology/stimupy/commit/9596b5ded530b7abb0415626cb0bc1bb30c3799e))

* improved constant phase-width in gratings despite rotation; removed weird code ([`399fcd6`](https://github.com/computational-psychology/stimupy/commit/399fcd6b2cee8bdd039cd4d11effc4f95f6c1f32))

* fixed bug to be able to change origin + phase shift ([`d2c4b3f`](https://github.com/computational-psychology/stimupy/commit/d2c4b3f9c9bdb5fa0821e95029443c9b868657e0))

* fixed bug that rotating inteferes with origin; cleaned code ([`99ffe88`](https://github.com/computational-psychology/stimupy/commit/99ffe88e9d192b5a717e76c8b5dd68b0ca71ac40))

* closes #93; extended use of origin - options: corner, mean, center ([`9da47f7`](https://github.com/computational-psychology/stimupy/commit/9da47f7890f2373c2e4e4acf58b4ff09c9b190e8))

* added roll-dict-util ([`4d20cb8`](https://github.com/computational-psychology/stimupy/commit/4d20cb87a63feceb7d52f5c27bae8d63e38cbb41))

* added phase_shift for square-wave and checkerboard ([`541fa63`](https://github.com/computational-psychology/stimupy/commit/541fa638298ea74dc97906e56a46fb2336d5b60a))

* checkerboard is now created as plaid ([`8ca9ca1`](https://github.com/computational-psychology/stimupy/commit/8ca9ca1d17187d466ddf858ca7877cffdaa850b9))

* small change ([`a0b60d4`](https://github.com/computational-psychology/stimupy/commit/a0b60d4d615fbdf10b43423956ac03211886e8e2))

* added documentation to edge components ([`7147bbd`](https://github.com/computational-psychology/stimupy/commit/7147bbd243fae18c07601126ac09ba63a7b73765))

* added Bessel function in circular components for modelfest ([`edd84ca`](https://github.com/computational-psychology/stimupy/commit/edd84ca57a3a48cf683b179f6fce84d1a0e27600))

* added binary noise for modelfest ([`a5fab8b`](https://github.com/computational-psychology/stimupy/commit/a5fab8bdf9fdbcec2b293213d74b9e3e326f554d))

* added edges-component and adapted scripts which contained edges ([`eeb7ff5`](https://github.com/computational-psychology/stimupy/commit/eeb7ff56a837f9307f30467a19f0e6fc58ccab77))

* added input variable for changing sine-wave / gabor origin ([`c34dfc5`](https://github.com/computational-psychology/stimupy/commit/c34dfc53c39672492a7f3f2ae9f70599fe230ec1))

* fixed bug for using gaussian windows in gabor ([`c1eb21e`](https://github.com/computational-psychology/stimupy/commit/c1eb21e56d6fadbbf888b6dcfda374cc7adb4373))

* fixed bug for low resolution for default target placement ([`d943680`](https://github.com/computational-psychology/stimupy/commit/d94368038e6b7c2fd7d430e4ac865c5a59dbc6c8))

* fixed wrong documentation and changed input order to visual_size, ppd, shape ([`56ee47d`](https://github.com/computational-psychology/stimupy/commit/56ee47d5d9836b8912ba8e2026012d4d5415217b))

* closes #89; general component Mondrian, updated related code ([`17058e9`](https://github.com/computational-psychology/stimupy/commit/17058e9c2576c46a94df3d86d55f3056047576a2))

* forced parallelograms to cover corners - hence updated RHS2007 corrugated mondrians ([`9b4c507`](https://github.com/computational-psychology/stimupy/commit/9b4c507c6a20a57616222d5ca56860dad3ba3fe8))

* corrected typos ([`535fc6f`](https://github.com/computational-psychology/stimupy/commit/535fc6f711b0abb6f3570e148e0bd7938f729b12))

* corrected bib-name ([`80dd437`](https://github.com/computational-psychology/stimupy/commit/80dd43735fc5e7e58de2ea385374208d51a1f6ff))

* first manuscript draft ([`c351d85`](https://github.com/computational-psychology/stimupy/commit/c351d850f9ee23e58f84d69512126396ada4b90b))

* closes #87, added luminance staircase ([`5c64b58`](https://github.com/computational-psychology/stimupy/commit/5c64b5846fa5f402503fbffb77675c3ed1d16eb1))

* updated grating use in illusions ([`84cd234`](https://github.com/computational-psychology/stimupy/commit/84cd2340de8c79f58acc395c20667a054252bde1))

* solved shape bug in gratings ([`d2ce712`](https://github.com/computational-psychology/stimupy/commit/d2ce712d34c4f84af6ac6e949e7fbc8caa491262))

* simplified code for calculating new shape - however, not working yet ([`b3a072d`](https://github.com/computational-psychology/stimupy/commit/b3a072d83c4998134b07566c6096139f855fba0e))

* closes #76, closes #79; created utils-contrat-conversions and added contrast changing functions including transparency ([`f180879`](https://github.com/computational-psychology/stimupy/commit/f1808793cef59be185504c05bd4a5762d63a2998))

* deleted old components backup ([`1e4f631`](https://github.com/computational-psychology/stimupy/commit/1e4f631a9748caf0f164fbf1f624b482f26306cd))

* Merge branch `rotated_gratings` into `main`

Rotated gratings, sinewaves, gabors

See merge request computational-psychology/stimuli!26 ([`02e4f0d`](https://github.com/computational-psychology/stimupy/commit/02e4f0db795708970d3843c8ecd33494948b15c6))

* Bugfix: convert to radians ([`efe979e`](https://github.com/computational-psychology/stimupy/commit/efe979e955fd580e5bdc0d43a5f145c845deffda))

* Calculate 2D size/shape from 1D, for rotated gratings ([`438e361`](https://github.com/computational-psychology/stimupy/commit/438e3617c39ebc088cac790cc2fa1f06fd8d341d))

* Merge branch `feat_unify_gratings` into `main`

Rounding grating parameters

See merge request computational-psychology/stimuli!25 ([`00b8949`](https://github.com/computational-psychology/stimupy/commit/00b8949199dfa308a51049f6ca35ea328276b0e2))

* Add round_phase_width flag

rounds phase_width to integer number of pixels. By default that's good behavior, but for angular gratings it isn't, so flag. ([`0095847`](https://github.com/computational-psychology/stimupy/commit/0095847348d7da2290a8047fac1ba912238dfde7))

* Update tests and paper stims ([`dc8d708`](https://github.com/computational-psychology/stimupy/commit/dc8d708cd1c305547906532f673e77b24a638b83))

* Cleanup resolve_grating_params ([`da55049`](https://github.com/computational-psychology/stimupy/commit/da550491d2be732f4605d2ac862d82aaeddce0e8))

* Docstring round_n_phases ([`b0b1594`](https://github.com/computational-psychology/stimupy/commit/b0b15940550f75a94875a83e3c76658d0207d112))

* Docstring factorize ([`95e53df`](https://github.com/computational-psychology/stimupy/commit/95e53df807a000334c3f893f38e12a69e828ef21))

* added first draft gabor ([`d7ace84`](https://github.com/computational-psychology/stimupy/commit/d7ace84f5a52c2e92fda9456642921a951c34c9a))

* added phase_shift input variable to sine-wave ([`175a3e1`](https://github.com/computational-psychology/stimupy/commit/175a3e16ccc328f0c923d37e47dae4108ebdb56b))

* first draft of rotatable gratings and sine-wave ([`34be9f8`](https://github.com/computational-psychology/stimupy/commit/34be9f86880b4ca94393a7c98662b2325655b61d))

* Merge branch `feat_shapes` into `main`

Move basic shapes to stimuli.components.shapes module

Closes #64 and #68

See merge request computational-psychology/stimuli!24 ([`5a6832a`](https://github.com/computational-psychology/stimupy/commit/5a6832a90527f22104350cf38a32c0c79a742da8))

* added new shapes to __all__ ([`d1d95d2`](https://github.com/computational-psychology/stimupy/commit/d1d95d2279bd6d0d241186275b15bd72a686c3e6))

* fixed bug in grating resolving and updated warnings ([`396ad39`](https://github.com/computational-psychology/stimupy/commit/396ad39ae1cff963fe85263a92f844f25e9acba1))

* Update testcases ([`217f2be`](https://github.com/computational-psychology/stimupy/commit/217f2be6c2b09c12d1e6dee07093d3d47d73eabc))

* Bugfixes ([`8eefe34`](https://github.com/computational-psychology/stimupy/commit/8eefe34b78e1a8066a2da1acc77c237cafe1b1f6))

* Use rounding of phases ([`83a92d6`](https://github.com/computational-psychology/stimupy/commit/83a92d61dd0d318d8bc940d9c3645258e75cd8b9))

* Helper function to round_n_phases ([`e461419`](https://github.com/computational-psychology/stimupy/commit/e461419969b1058913c7de3911ecfe17961d70b7))

* Util for integer factorization

not very efficient, but should be good enough for our purposes ([`83bd0e6`](https://github.com/computational-psychology/stimupy/commit/83bd0e6a3a16bbd2af39345fb12d60d267925fe9))

* first draft even, odd etc period in grating ([`e096a15`](https://github.com/computational-psychology/stimupy/commit/e096a15532dbf35eb914359f4d44e323e360d39f))

* Also import disc, ring, annulus, and wedge in shapes ([`c8116a3`](https://github.com/computational-psychology/stimupy/commit/c8116a33fff698b7526b1af67e2a11af67693394))

* Also moved transparency to shapes ([`12953fe`](https://github.com/computational-psychology/stimupy/commit/12953fecdcfb4f00886f63e975cde1ad870423df))

* Fix overview ([`6cd3f5a`](https://github.com/computational-psychology/stimupy/commit/6cd3f5ad040d6d18e33a91dfa2038f5f418d8489))

* Parallelogram_depth not optional

Other arguments default to None,
closes #64 ([`031b342`](https://github.com/computational-psychology/stimupy/commit/031b34254cfbfe8323a7bd27b59d53d0846af7da))

* Shapes no longer needs degrees_to_pixels ([`f8bef1d`](https://github.com/computational-psychology/stimupy/commit/f8bef1d7a80e5712186f4ba971e50a2ece2eb61f))

* Demo cross ([`c65b569`](https://github.com/computational-psychology/stimupy/commit/c65b5691e58c912c080e8acaecd892c1e91652b3))

* Cross uses resolution resolving ([`1b8cc94`](https://github.com/computational-psychology/stimupy/commit/1b8cc941f0e164816dfa4f4dd815c806a48fe295))

* Demo parallelogram ([`61474a9`](https://github.com/computational-psychology/stimupy/commit/61474a9e47ae7171914032d49cfa3b6fa52f19b6))

* Parallelogram uses resolution resolving ([`962e269`](https://github.com/computational-psychology/stimupy/commit/962e269534c9b879610c74578df96b315d4946b6))

* Demo triangle ([`6812abb`](https://github.com/computational-psychology/stimupy/commit/6812abb7fc4d515eb258a6f0da91d98643a23055))

* Triangle uses resolution resolving ([`a9e05e8`](https://github.com/computational-psychology/stimupy/commit/a9e05e865ebfdd0bfc0ba319bd190ec742c76689))

* &#34;Fix&#34; rounding RHS2007.todorovic_in_large ([`0fec90b`](https://github.com/computational-psychology/stimupy/commit/0fec90b329ac5b0b6be8f6408a4eb51fe10684e0))

* Rectangle component uses resolution resolving ([`5c2cb6a`](https://github.com/computational-psychology/stimupy/commit/5c2cb6af365de59bdf303dcb4a2fa2d6dbb8d4a3))

* Move basic shapes to components.shapes

Closes #68 ([`b48467f`](https://github.com/computational-psychology/stimupy/commit/b48467fbfa1d16249c92fb54a60ecba688f9f65f))

* Update Murray2020 checkassim ground truth for mask

... all ints ([`1b70e79`](https://github.com/computational-psychology/stimupy/commit/1b70e796950d8914bad90c4d58a8cf184728d142))

* Merge branch `feat_unify_gratings` into `main`

Unify some of the grating resolving

See merge request computational-psychology/stimuli!23 ([`dfe48a3`](https://github.com/computational-psychology/stimupy/commit/dfe48a31f1261d0c00387baa5be0c2050f0c79ac))

* Bugfix: Linear grating uses draw_regions ([`620f036`](https://github.com/computational-psychology/stimupy/commit/620f036d82db2757b7412f7c530c671b75929622))

* Frames demo: can select any grating arguments ([`9a35b79`](https://github.com/computational-psychology/stimupy/commit/9a35b79254c3cb66ba83fc5f6740ea371756dbbe))

* Bugfix: ensure that order of grating intensities always stays the same ([`1bb480f`](https://github.com/computational-psychology/stimupy/commit/1bb480fe3b3356388a568995b2a802234e86b2bf))

* closes #50; added padding utils for dicts ([`4993133`](https://github.com/computational-psychology/stimupy/commit/4993133a6b8351a321943cd2e342dab5c97afb62))

* added size resolving to most stimuli ([`757b0f1`](https://github.com/computational-psychology/stimupy/commit/757b0f128a9d5d046ee8c0ba046308d257eaa10d))

* Bugfix: disc radius can be used as image size ([`2751519`](https://github.com/computational-psychology/stimupy/commit/27515197a0e245cad53ef580706263d00ea5281b))

* Bugfix: mask_elements correctly gets shape ([`3670b78`](https://github.com/computational-psychology/stimupy/commit/3670b789e2c95667294aa17e9f054c80ad116ef9))

* Bugfix: frame_widths ([`4ad676f`](https://github.com/computational-psychology/stimupy/commit/4ad676f8650446c81e60b5b5ed3080d3e9ca4f66))

* Minor cleanup ([`7f7a188`](https://github.com/computational-psychology/stimupy/commit/7f7a188ceba2b2e98797820489104c6e4eaac877))

* Use mask_elements for linear gratings ([`83d37a3`](https://github.com/computational-psychology/stimupy/commit/83d37a35ff77f086fbfc37a2de8dc2f85a963e9c))

* Better handling of 0 visual sizes ([`15e1412`](https://github.com/computational-psychology/stimupy/commit/15e14127a7099936981b8f3d7426a751a7ac8c94))

* Add origin to mask_elements ([`95ae23f`](https://github.com/computational-psychology/stimupy/commit/95ae23fc5a56595faded02dc3c195f3a1d38ae12))

* Docstring image_base ([`0560fc2`](https://github.com/computational-psychology/stimupy/commit/0560fc242bc156227e78fb33935ba51020c0ebd5))

* Interactive demo for image_base ([`36899f5`](https://github.com/computational-psychology/stimupy/commit/36899f5a43d245afc0d9b0be60de37ea3be444f6))

* Add origin argument to image_base ([`0b787f9`](https://github.com/computational-psychology/stimupy/commit/0b787f93ce2f3d8e57d70d7ceb2861bb63d9c86c))

* Move to stimuli.components: image_base, resolve_grating_params, draw_regions ([`aa5dcb8`](https://github.com/computational-psychology/stimupy/commit/aa5dcb89533134f62d2f85f20dcda0025e7501d0))

* Extract components.mask_elements()

others just wrap around it ([`772b854`](https://github.com/computational-psychology/stimupy/commit/772b854007dd39cc134e342b3422a3d60b922fd3))

* Pinwheel: use `mask` of disc to mask, not `img` ([`0aba9be`](https://github.com/computational-psychology/stimupy/commit/0aba9be2d8b0f9bed4fc6bda278e325b4e68cd97))

* Unify `mask_[element]s` functions

...mostly. For linear gratings (&#34;horizontal&#34;/&#34;vertical&#34; orientation), still need to shift distances... ([`df8b164`](https://github.com/computational-psychology/stimupy/commit/df8b164a35f2e5e3566e379fc1e5d83ff8de1a38))

* Bugfix: demo image base ([`1a05d4c`](https://github.com/computational-psychology/stimupy/commit/1a05d4cc6047d5acc63e38e74de2a01858b727ec))

* Unify intensity arguments

intensity_[element],
defaults as tuple (not mutable list)
defaults for square-waves (1.0, 0.0): first phase is up, in line with sinewave ([`b37a1fa`](https://github.com/computational-psychology/stimupy/commit/b37a1fa44212dc59f99ddb20ecf48f269f758e68))

* Update grating_params demo for frames ([`1d88ae3`](https://github.com/computational-psychology/stimupy/commit/1d88ae373a1981f39f3e442dc8d4a73ce3543108))

* frame_widths argument not optional in components.frames() ([`5d6803b`](https://github.com/computational-psychology/stimupy/commit/5d6803b6263197426d147b0bd7bc002beb9425f3))

* Update RHS2007 ground truth for bullseye illusions

...since the frame drawing has changed slightly ([`005be80`](https://github.com/computational-psychology/stimupy/commit/005be8091096729176dde1923afdd15ec219f300))

* Better deal with rounding issues ([`e36b337`](https://github.com/computational-psychology/stimupy/commit/e36b337f302b3d76615dfed7687528951218a561))

* Update angular demo ([`edead73`](https://github.com/computational-psychology/stimupy/commit/edead73b05b1f668244e72ae07954ffe17f3f63a))

* Mask_segments uses identical code to other mask_[element]s ([`fb67052`](https://github.com/computational-psychology/stimupy/commit/fb670528b1c66a3d94bcb33e50ffa8f4785da5b0))

* Separate mask_segments, drawing ([`971986b`](https://github.com/computational-psychology/stimupy/commit/971986bbbf89a1ab622dac6395402e0618622ea0))

* More variable renaming ([`6bbb456`](https://github.com/computational-psychology/stimupy/commit/6bbb456bee7aea3fd395041c753006d5e0a1a9da))

* Minor changes ([`1594120`](https://github.com/computational-psychology/stimupy/commit/1594120ec37d5377f0da2775f888b9ec29786865))

* angular segments, some variable renaming ([`72f44e3`](https://github.com/computational-psychology/stimupy/commit/72f44e3ff9e0f9ade2c740985a14a90b611e2e6d))

* Update frames demo ([`8b74417`](https://github.com/computational-psychology/stimupy/commit/8b74417bed58c7efb027bd994aab64f9a86cb00c))

* Cleanup frames a bit ([`fd1b0ac`](https://github.com/computational-psychology/stimupy/commit/fd1b0ac6164f1bf0030e3525720b9fe8c5d7ae6f))

* Also output shape in image_base ([`ef2e7ee`](https://github.com/computational-psychology/stimupy/commit/ef2e7ee2a5cfa61a852e2a4a9ecf40f18f148c31))

* Docstrings ([`a2af69d`](https://github.com/computational-psychology/stimupy/commit/a2af69d677368b96a854b9980db00fe50564d277))

* Separate drawing frames, from drawing ortholinear grating ([`c0c907d`](https://github.com/computational-psychology/stimupy/commit/c0c907d8d1b1229fca97eb3daa3a14717a3c8b61))

* Function for creating image from mask and intensities ([`b72727e`](https://github.com/computational-psychology/stimupy/commit/b72727e4ca080cc16e24a5de3f9254d14b2e5fbd))

* Clean up components.components ([`2b5e5c7`](https://github.com/computational-psychology/stimupy/commit/2b5e5c7ce8b013bccb80a9c5d9c2cd3b883f9caf))

* Separate masking of bars, and drawing linear square_wave grating ([`85f190a`](https://github.com/computational-psychology/stimupy/commit/85f190a94c80947aa83ab529c80189dc43daa1a9))

* If None, set largest radius of ring to visual_size max ([`7402a14`](https://github.com/computational-psychology/stimupy/commit/7402a14e256b1baf3f500459f85e54495b685d42))

* Add pinwheel to demo ([`8359723`](https://github.com/computational-psychology/stimupy/commit/835972368ac898a8bc891ef5a6523b9b2f565dc2))

* Clean out angular demo ([`0f0200e`](https://github.com/computational-psychology/stimupy/commit/0f0200e88b7d58d4216e2e8e16bb84f8516d5957))

* Angular grating uses resolve_grating_params ([`e19c695`](https://github.com/computational-psychology/stimupy/commit/e19c695e5f7924ebf4a78cd8d878f73e8a17b1e6))

* Angular uses image-base ([`a245ff2`](https://github.com/computational-psychology/stimupy/commit/a245ff26d6a60ea70df75bdcdeee7ee4241f5b85))

* Image-base docstring ([`e0e72ad`](https://github.com/computational-psychology/stimupy/commit/e0e72ad9175abe12cf02dd1240f1e6e80c9bda18))

* Image-base also rotates ([`2e1df0d`](https://github.com/computational-psychology/stimupy/commit/2e1df0df3b3c3ad7eefc78dc899e4f34bff2b6c2))

* Add circular grating to demo ([`6b91667`](https://github.com/computational-psychology/stimupy/commit/6b91667e5396b5a70877025b25ef8bd8031e1fe9))

* Circular uses image_base ([`473d35e`](https://github.com/computational-psychology/stimupy/commit/473d35e72ffb9dbcb8d0b89e200d73d6eb5debae))

* resolve_grating also does edge-cases ([`847acac`](https://github.com/computational-psychology/stimupy/commit/847acacf248e37dd736ae539d26e07c8abf9b909))

* Grating, frames, use image_base ([`f7009ec`](https://github.com/computational-psychology/stimupy/commit/f7009ecb8b1a5d2a8b7aae9bf85de2fa481b937f))

* resolve_grating_params also outputs edges ([`748dcb0`](https://github.com/computational-psychology/stimupy/commit/748dcb048a3be6973de26ec1d787767171e57906))

* Rename xx, yy to horizontal, vertical (in line with &#34;distiance&#34;) ([`3aa597f`](https://github.com/computational-psychology/stimupy/commit/3aa597ff3289bc043792447396eedd03c9350778))

* Demo image_base / dimensions ([`3600a96`](https://github.com/computational-psychology/stimupy/commit/3600a96cf5d1f927a131168d0c4c436cb0d95873))

* image_base component ([`3b14bb5`](https://github.com/computational-psychology/stimupy/commit/3b14bb5eaa0f6750efe4525262078c6f9e575ff2))

* Demo linear gratings, frames ([`f1afdcf`](https://github.com/computational-psychology/stimupy/commit/f1afdcf76c3b051a7e9fcbb6a992a863c29210aa))

* Demo resolving grating params ([`b2653bd`](https://github.com/computational-psychology/stimupy/commit/b2653bdbedff25ada21fa2c1e32b3c7d2298e4fc))

* Move resolve_grating_params to components ([`1e1da01`](https://github.com/computational-psychology/stimupy/commit/1e1da01d663ff903012e67ecb6504ae8fec0356b))

* added gaussian component ([`718c451`](https://github.com/computational-psychology/stimupy/commit/718c4515abcf719b8ab780cbcf4a1225a264e232))

* added todorovic_equal illusion ([`760da79`](https://github.com/computational-psychology/stimupy/commit/760da796e74b6e952349908f4a6903f65e20593c))

* closes #25; add original source to illusions ([`aed377e`](https://github.com/computational-psychology/stimupy/commit/aed377ef4e6024ab77b35bb85d55e6f7757b9ca7))

* closes #61, closes #59; working overviews, removed default params from functions ([`a3a7797`](https://github.com/computational-psychology/stimupy/commit/a3a7797feab9e527fbd8046f90825c4c6981cf32))

* changed variable name ([`d395983`](https://github.com/computational-psychology/stimupy/commit/d3959830b3b4ab8abbed2d30a4990672599a880f))

* changed cube implementations ([`0e01424`](https://github.com/computational-psychology/stimupy/commit/0e014247208d95831fdb87478f7dfa19269d69b4))

* reorganized dungeon and added resolving ([`ea0f1df`](https://github.com/computational-psychology/stimupy/commit/ea0f1df867ecd104eba9d32933a0c0c5650d23ae))

* fixed that checkerboard-add_targets converts masks to float ([`b12cf75`](https://github.com/computational-psychology/stimupy/commit/b12cf7561dda758e366192a822c4185effac1984))

* made masks int and added mask=None if no target is added ([`989c42f`](https://github.com/computational-psychology/stimupy/commit/989c42f4483f6062891bca6b7afbc20ef2b6df56))

* removed irrelevant tests ([`4861661`](https://github.com/computational-psychology/stimupy/commit/486166182a33de00142a514310a19527927a7e4b))

* fixed small bug that mask was not int ([`5572ac9`](https://github.com/computational-psychology/stimupy/commit/5572ac999b05d5ce6c95b084bb409ab8bd36567f))

* Also removed test_contrast_metrics ([`d636569`](https://github.com/computational-psychology/stimupy/commit/d636569c994ec6ad9410112fd875562ac256da54))

* closes #62, closes #60; fixed bugs in sbc-general and todorovic-cross ([`07e1200`](https://github.com/computational-psychology/stimupy/commit/07e12008ba3c46189f516d4d397dc209359236c5))

* closes #15; updated plot_stim(uli) and all scripts that use them; added to_img() ([`78e400e`](https://github.com/computational-psychology/stimupy/commit/78e400e4b90e2b04641d7ab4899d1d3a872e55d4))

* added all .ipynb_checkpoints to gitignore ([`3056654`](https://github.com/computational-psychology/stimupy/commit/3056654239119d925e523991c8918ee3df035865))

* closes #58, added __all__ to all scripts, re-structured pink noise into one_over_frequency noise ([`289a3c8`](https://github.com/computational-psychology/stimupy/commit/289a3c857e3a771bfa6e634be728cd25c4d215fa))

* removed contrast_metric, transparency, texture from init ([`9391e5d`](https://github.com/computational-psychology/stimupy/commit/9391e5d93d518584c817d5786c8666d8091fc039))

* closes #7, closes #57; removed contrast_metric, transparency and texture from main branch ([`324b08f`](https://github.com/computational-psychology/stimupy/commit/324b08fccfd8ad6a82760e825b71f0b6f45e2e25))

* added scripts for white1981 and 1985 ([`293c16d`](https://github.com/computational-psychology/stimupy/commit/293c16d16ac183608494c9687c9355f80ea0a7a5))

* fixed alignment bug in grating_grating when rectangle is too large ([`59ee907`](https://github.com/computational-psychology/stimupy/commit/59ee9074fd6f49cba690cb96bab3659c3f66a07e))

* fixed bug in grating_grating that rectangle and gratings could have different shapes + made masks ints ([`93c6b92`](https://github.com/computational-psychology/stimupy/commit/93c6b92d7fefab261ab73144b52ffa30e69c0b93))

* Rename RHS2007 checkerboard stimuli

Names match paper (except for omitting the decimal point)
Closes #14 ([`dd6d526`](https://github.com/computational-psychology/stimupy/commit/dd6d5261382e7cb4424cca967ad88599c121288c))

* corrected bug - removed rings from init ([`6a0ed3e`](https://github.com/computational-psychology/stimupy/commit/6a0ed3eac234caed25d8c4d47821237ca1f07eab))

* Merge branch `feat_frames` into `main`

Frame-like stimuli

Closes #41, #39, #40, and #47

See merge request computational-psychology/stimuli!22 ([`9b9d32e`](https://github.com/computational-psychology/stimupy/commit/9b9d32eeb5b9ea5a2b126bcf498dc1d7feeb44a8))

* Merge branch `feat_gratings` into `main`

Gratings (square-wave)

Closes #47

See merge request computational-psychology/stimuli!21 ([`d7472f6`](https://github.com/computational-psychology/stimupy/commit/d7472f6124631eebf9fe5cadbeba39412f41c7a7))

* Attempt to update paper stimuli and remove vestigials

Not quite replicating though.... ([`9e4c10c`](https://github.com/computational-psychology/stimupy/commit/9e4c10c0b6007e0fff9675845d8347e829bfc147))

* Demo for frames.bullseye ([`576ee2f`](https://github.com/computational-psychology/stimupy/commit/576ee2f76dee825c57883815c318779cdc6c6228))

* frames.bullseye ([`1b1b35c`](https://github.com/computational-psychology/stimupy/commit/1b1b35c2fe187925ed897f90e6dc26d46c208606))

* Bugfix: frames component

Flexibly resolve resolutions ([`1d80c01`](https://github.com/computational-psychology/stimupy/commit/1d80c019b46e8ae45447a461a6a1c2090290053b))

* Demo for frames component and illusion ([`8b7232b`](https://github.com/computational-psychology/stimupy/commit/8b7232b51e28e37ca0671e1523f2e8520c26b5ca))

* illusion.frames

Closes #41 ([`fe83ad9`](https://github.com/computational-psychology/stimupy/commit/fe83ad9d0e8c0434dd86499bdcaf35191d9d09b2))

* Component for square frames

Closes #39, #40 ([`e00eee5`](https://github.com/computational-psychology/stimupy/commit/e00eee54101f84611caac8cece7f17f056e245b0))

* Include grating_induction and grating_grating_shifted in demo ([`f759c2f`](https://github.com/computational-psychology/stimupy/commit/f759c2f7f645b09840386aceb3cbe4216fa97664))

* Update grating_induction ([`b003116`](https://github.com/computational-psychology/stimupy/commit/b0031168bd919680d20138d884d0239b49b19c00))

* Incorporate grating_induction ([`9b6dfe2`](https://github.com/computational-psychology/stimupy/commit/9b6dfe23f81a699c4e94c06a2066c74623ecd531))

* Remove vestigial square_wave_grating ([`4987c4a`](https://github.com/computational-psychology/stimupy/commit/4987c4ad8f78a958968f571d36ab1179132fda39))

* Cleanup ([`ea7e0b2`](https://github.com/computational-psychology/stimupy/commit/ea7e0b2f8ead615a40996b291ce8acfa8b289846))

* Update grating_grating_shifted ([`8224b10`](https://github.com/computational-psychology/stimupy/commit/8224b1001bb012527ef3c6a725393ddf58e6f8c3))

* Update grating_grating ([`97d51ca`](https://github.com/computational-psychology/stimupy/commit/97d51ca1e3f2d3ee949d7b611d8cbbe429bcaf69))

* No default targets ([`f3a1031`](https://github.com/computational-psychology/stimupy/commit/f3a1031c3c8bbac471fd2e473f816aedbae41111))

* Update grating_uniform ([`0f8cbc2`](https://github.com/computational-psychology/stimupy/commit/0f8cbc26e6a306188105491c9ec6d1015d7f019d))

* Demo for square_wave `illusion` ([`8646629`](https://github.com/computational-psychology/stimupy/commit/8646629cf860e833da7cc9adbc1a64b6277b0b04))

* Rename and update square_wave `illusion` to use square_wave component ([`2b57463`](https://github.com/computational-psychology/stimupy/commit/2b574635d63c6d11c940f9d2428ece4846e044a3))

* Update docstrings ([`18431b1`](https://github.com/computational-psychology/stimupy/commit/18431b10ecd4283b726e2eface816f56b25efc79))

* Bugfix demo ([`34e3a1c`](https://github.com/computational-psychology/stimupy/commit/34e3a1cf049fc556bdeda0fdcf5106e83ffd1bff))

* Bugfix: plotting masks ([`ea69405`](https://github.com/computational-psychology/stimupy/commit/ea69405d6f34105f877c73e8ab28cbe7c5b265db))

* Add orientation to demo ([`fff029c`](https://github.com/computational-psychology/stimupy/commit/fff029c8716f068a757208e850e7e8b38cacb95e))

* Add orientation to square_wave component ([`9ff5628`](https://github.com/computational-psychology/stimupy/commit/9ff5628ab079248ed5da2dd7087f3cdb5e33c86d))

* Demo for grating component ([`3d75063`](https://github.com/computational-psychology/stimupy/commit/3d75063a7d1f7f9cc2b4504cece87a3b25ef9f01))

* Grating component outputs stim_dict ([`ba65627`](https://github.com/computational-psychology/stimupy/commit/ba656272bf59961dc7435bb1222c013e7146b0ae))

* Optionally round number of phases ([`ce11bd4`](https://github.com/computational-psychology/stimupy/commit/ce11bd463de4934c95fa44e98b26d8883f1d4940))

* Resolve grating params in 1D

Closes #47 ([`ebd02e5`](https://github.com/computational-psychology/stimupy/commit/ebd02e51d7951184422cfbcd888ec108d634b5b5))

* fixed small typo in general documentation ([`62668f6`](https://github.com/computational-psychology/stimupy/commit/62668f6667ccd482a9c23084517bdebcd8704153))

* Separate generating of mask as prestep for generating square wave ([`463069c`](https://github.com/computational-psychology/stimupy/commit/463069c0e4728f60cab18cf6ac836c62b92e0894))

* Rounding of pixels optional in resolution ([`6b958a9`](https://github.com/computational-psychology/stimupy/commit/6b958a9190b539492596ab4a8ffa890590a3fc8d))

* Rename argument ([`b3c8c25`](https://github.com/computational-psychology/stimupy/commit/b3c8c25ab489abbdf23c58dd6cfe39e30f29c669))

* Use utils.resolution to resolve resolution params ([`f6c0006`](https://github.com/computational-psychology/stimupy/commit/f6c00066cd560eabbbe3c7fee286c391e98a59d2))

* Tests for resolving grating params ([`f578899`](https://github.com/computational-psychology/stimupy/commit/f578899cf2fdafd0a0eba4544549b442c5ec5c8f))

* Function for resolving grating params ([`06e22e2`](https://github.com/computational-psychology/stimupy/commit/06e22e21c5066b804b90bc614fc10dc8d553e391))

* Extract  squarewave (grating) to separate component ([`507ef5d`](https://github.com/computational-psychology/stimupy/commit/507ef5d604d2d694b1c3f7f879627689e6fbf63b))

* closes #33, closes #48; all components return dicts; updated variable names and improved consistency ([`1aae8f9`](https://github.com/computational-psychology/stimupy/commit/1aae8f9606d7163804a09a36f82719eebcf969ff))

* added new version of wedding cake ([`d2245db`](https://github.com/computational-psychology/stimupy/commit/d2245db1b071d1b8f90b67e7d91ec5356657dc66))

* fixed problem in todorovic that precision affected target placement ([`ee9d0f7`](https://github.com/computational-psychology/stimupy/commit/ee9d0f7c71c70b10616bc49451fb88e2120e6b65))

* Merge branch `feat_circular` into `main`

Circular and angular stimuli

Closes #36 and #37

See merge request computational-psychology/stimuli!19 ([`944629d`](https://github.com/computational-psychology/stimupy/commit/944629dcf5d5c6717fe9d63a3a9c093e72952de0))

* Merge branch `feat_utils` into `main`

Utils for getting masked values, averages, etc.

See merge request computational-psychology/stimuli!20 ([`b04feb6`](https://github.com/computational-psychology/stimupy/commit/b04feb604f1c1993c4abcf946e7916dc767e5174))

* Merge branch `feat_domijan` into `main`

Solve resolution for Domijan2015

Closes #32

See merge request computational-psychology/stimuli!18 ([`23c251c`](https://github.com/computational-psychology/stimupy/commit/23c251cf1a54c5bfbdc03b3ed058780e5b3dcd7c))

* Bugfix angular demo: wedge(angle) -&gt; wedge(width) ([`40cacd1`](https://github.com/computational-psychology/stimupy/commit/40cacd12004bef5319a1f16d5f4d1ec434ad68c5))

* Bugfix circular demo: circular_grating is now called circular.grating ([`ab34f31`](https://github.com/computational-psychology/stimupy/commit/ab34f313ef29758c1f1229d3bd8e7c42d226c7ef))

* Use colormap to decide mask-indices when plotting mask ([`dfbb3c7`](https://github.com/computational-psychology/stimupy/commit/dfbb3c77d8d233c7f7035b5ed1eb93b8de6cc5cc))

* Add utils for getting masked values, average target values, etc.

These originally come from BRENCH.postprocessing.utils ([`b319349`](https://github.com/computational-psychology/stimupy/commit/b319349f436cba5c5b532babd852a8f9f3f76006))

* remove &amp; ignore .ipynb checkpoints ([`72377ed`](https://github.com/computational-psychology/stimupy/commit/72377ed809e9d5039c4df2639d79acaadcf5440f))

* Rename circular_grating() -&gt; circular.grating() ([`ec4e298`](https://github.com/computational-psychology/stimupy/commit/ec4e29843b0e59e424eebcb8e504692a6d08d798))

* docstrings ([`5f8c2f9`](https://github.com/computational-psychology/stimupy/commit/5f8c2f9fbb29e95b42eecc909520e8c96a640511))

* Update Demo radial_white ([`99e41ff`](https://github.com/computational-psychology/stimupy/commit/99e41ff23a2ae35ca3b78b45a37b05e9d80393d2))

* Update RHS2007 ([`518dd82`](https://github.com/computational-psychology/stimupy/commit/518dd8219f13648474428efed84708b2b5799c83))

* Fix angles ([`8b804ca`](https://github.com/computational-psychology/stimupy/commit/8b804ca10184628e517e13dd4cd79f611a41312b))

* Update illusions.angular.radial_white to use pinwheel component ([`becdee9`](https://github.com/computational-psychology/stimupy/commit/becdee9671c365ff5ef6b9b743fc6809cbb7278f))

* Move radial_white to illusions.angular ([`0ce2a6d`](https://github.com/computational-psychology/stimupy/commit/0ce2a6d8176132f9671644f094ce5ffd257d54b4))

* Merge branch `feat_angular` into feat_circular ([`ba48d57`](https://github.com/computational-psychology/stimupy/commit/ba48d57ea61289a4cd879578ad21dce6c58adf08))

* Update and expand Demos ([`1e3d912`](https://github.com/computational-psychology/stimupy/commit/1e3d91287deaceda480558fc258d5d6b878acba3))

* Propagate rotation argument through components ([`34effb3`](https://github.com/computational-psychology/stimupy/commit/34effb3777d0b6726e81114a3704521fbbade2da))

* img_angles returns stim_dict ([`65005b5`](https://github.com/computational-psychology/stimupy/commit/65005b52f453907ab9acbe1a3574d160d83d684a))

* Demo for pinwheel ([`74c7e8d`](https://github.com/computational-psychology/stimupy/commit/74c7e8d4a3cf7361b41d969c5e83c72e67330f33))

* Pinwheel component ([`ed9421a`](https://github.com/computational-psychology/stimupy/commit/ed9421abbb69abb91e020bf5910b3133dd9eab62))

* Update docstring ([`510e6fe`](https://github.com/computational-psychology/stimupy/commit/510e6feed26abcd10196744c1fcc488cc33fb7ef))

* Demo angular grating ([`c579a06`](https://github.com/computational-psychology/stimupy/commit/c579a065517b4f1012589626f9259031cd560a52))

* angular.grating ([`a2a6e42`](https://github.com/computational-psychology/stimupy/commit/a2a6e4221dd93476e08b8db99c9eb3674cd035cf))

* Bugfix: angles ([`c3e469c`](https://github.com/computational-psychology/stimupy/commit/c3e469cc440cf66f961712b37c8616ec02c48a19))

* No drawing of background necessary ([`2f8f024`](https://github.com/computational-psychology/stimupy/commit/2f8f024dfe56797c7d7671a35c9ccf9382cc2b37))

* Get rid of supersampling ([`aca614d`](https://github.com/computational-psychology/stimupy/commit/aca614d9c90a26f42f3ee85c85407da7771b0cb6))

* Demo for angular segments ([`acdeee2`](https://github.com/computational-psychology/stimupy/commit/acdeee204d75f7f5bdd865948be30c28fc1dbe44))

* Change segment_masks into angular_segments ([`f4e8971`](https://github.com/computational-psychology/stimupy/commit/f4e8971ae582dc1e8b2ccb2e07cdac0fd4043abc))

* Resolve angular grating params ([`4aabae1`](https://github.com/computational-psychology/stimupy/commit/4aabae15b7e828074711e70dfdc770de02397f86))

* Angular segment masks ([`a3b0f36`](https://github.com/computational-psychology/stimupy/commit/a3b0f36b11f21ff88e577f1e993ace66f5ff12c1))

* type docstring ([`a07a895`](https://github.com/computational-psychology/stimupy/commit/a07a8950237c3e716b56264c4d368d30c83fed59))

* Demo wedge ([`33b44de`](https://github.com/computational-psychology/stimupy/commit/33b44def01c82ad93cbacd593a8f8fff5d3328b1))

* Component to draw a wedge (circle segment) ([`d7b5c4c`](https://github.com/computational-psychology/stimupy/commit/d7b5c4cd796881bce364fae66237e6282a7e06e8))

* component to mask a contiguous segment of angles ([`a8ed843`](https://github.com/computational-psychology/stimupy/commit/a8ed843abc3ef4d2b78fccd7cbbbc1d8865913f5))

* Demo for angles ([`e882208`](https://github.com/computational-psychology/stimupy/commit/e8822081c15a19040259f08a79420c7fd605495a))

* function for getting angle at each point ([`91c702f`](https://github.com/computational-psychology/stimupy/commit/91c702fd2d166cb97f7c4a8e66bc92462eb3450b))

* components.disc uses components.ring ([`628cca8`](https://github.com/computational-psychology/stimupy/commit/628cca882fb2d9ca8360185524639eb30ca33cb9))

* Update demos for illusions.circular_white, .bullseye ([`2e02513`](https://github.com/computational-psychology/stimupy/commit/2e02513be722861679dccb5f3f6e8e2c11525313))

* Add ring_width, n_rings as (optional) arguments to circular illusions ([`34582ba`](https://github.com/computational-psychology/stimupy/commit/34582ba5309a8fbe31750e80247c93f4b59b7056))

* Default intensities as floats ([`3452f78`](https://github.com/computational-psychology/stimupy/commit/3452f783d46c4ca50e54778efd78c69f3b8240eb))

* Paper stimuli specify supersampling=1 ([`0cbd4fc`](https://github.com/computational-psychology/stimupy/commit/0cbd4fce1b3c957b6604764c69d3f7905403bd81))

* Rename params ([`cf5a84a`](https://github.com/computational-psychology/stimupy/commit/cf5a84ab021194d196e063d14467c6e49d2e2dc2))

* Update circular_white, circular_bullseye ([`46b448a`](https://github.com/computational-psychology/stimupy/commit/46b448a6e3ff9beed501bfd8ce163e7db07e5ecb))

* Default supersampling factor = 1 ([`16e1f72`](https://github.com/computational-psychology/stimupy/commit/16e1f7226d6a664f89ba34fc16bff09b713a0249))

* Demo for grating only frequency, not n_rings ([`0caf4d1`](https://github.com/computational-psychology/stimupy/commit/0caf4d1e79e6223c4fc7be7bc01a4b8cc01c5a34))

* intensity_background 0.5 by default ([`5203980`](https://github.com/computational-psychology/stimupy/commit/5203980766981bf5fa5b8752b015a3224f8a7b17))

* Function defining ring masks ([`f077602`](https://github.com/computational-psychology/stimupy/commit/f077602b47619bb4a996b8eeeba3d8cea98ae160))

* Demos for components ([`70aa8fb`](https://github.com/computational-psychology/stimupy/commit/70aa8fb6ed19cd89e4641fd0a3339b29a47d0b57))

* Bugfixes: resolving/checking of ring_widths

Also fix test ([`dfa91c2`](https://github.com/computational-psychology/stimupy/commit/dfa91c25a4b87c7e8e2a0b9a9858349734b597d3))

* Better resolving/checking of visual_size ([`3261d95`](https://github.com/computational-psychology/stimupy/commit/3261d95f27893ee6f2c7f124cf3051af647e0b95))

* Rename intensity_background ([`0c94b80`](https://github.com/computational-psychology/stimupy/commit/0c94b8017ec1aded823f2211f26efe29ac4ff351))

* Circular grating ([`62f9424`](https://github.com/computational-psychology/stimupy/commit/62f9424e1d6eefb828efed21fb6d17f9ba733a86))

* docstrings disc, ring ([`bc87232`](https://github.com/computational-psychology/stimupy/commit/bc87232a1267ebf3f5279e2bbedd18a75ef7ebfc))

* resolve_circular_params ([`5d9f1e3`](https://github.com/computational-psychology/stimupy/commit/5d9f1e30c115402c7879b907783a82f6f3dfb17c))

* Add disc, ring, annulus demos ([`fa67dce`](https://github.com/computational-psychology/stimupy/commit/fa67dce5c97e48a7749887a8683056990c3b3f68))

* Disc, ring, annulus

Closes #37 ([`16ebcbf`](https://github.com/computational-psychology/stimupy/commit/16ebcbfd6ccc531cc1b511eaafaa51a28ee1bf5d))

* Rename background -&gt; background_intensity ([`9a62dd0`](https://github.com/computational-psychology/stimupy/commit/9a62dd0d2c7cbe6675a9953053ec4cf902fb9176))

* Add demo of disc_and_rings to Notebook ([`82fb2a6`](https://github.com/computational-psychology/stimupy/commit/82fb2a6ba6122369b0c15917c07b0bdc78204103))

* Ensure correctly drawing from outside -&gt; in ([`32f14cd`](https://github.com/computational-psychology/stimupy/commit/32f14cd4cd80a9be1f96e29161cfb74d10f78bf7))

* Some renaming ([`fd6862a`](https://github.com/computational-psychology/stimupy/commit/fd6862a431a52cd3c2fa93ba4516135982a09928))

* Output dict by disc_and_rings ([`f8ae906`](https://github.com/computational-psychology/stimupy/commit/f8ae9063fd65f6398b43d025ca4d9d51b4f63767))

* Resolve resolution for disc_and_rings ([`e59ed06`](https://github.com/computational-psychology/stimupy/commit/e59ed06c0b6ca49a7482147016ca341b26a98a21))

* Rename, add and document arguments to disc_and_rings ([`02ad7f7`](https://github.com/computational-psychology/stimupy/commit/02ad7f72a638c6b8fc8235fef29d787c6b0ba825))

* Extract disc, rings, to separate components.circular ([`97aaeef`](https://github.com/computational-psychology/stimupy/commit/97aaeefc90598d7bc5fca5bea0199949f19e5ff1))

* Bugfix: don't auto-import utils.utils ([`d70b13f`](https://github.com/computational-psychology/stimupy/commit/d70b13f4cd92cd16f7f7504e382f5df001ee9168))

* Update docstrings ([`4ccae85`](https://github.com/computational-psychology/stimupy/commit/4ccae85a8815ea2afbd9bb29edaf65f5ef7fc410))

* Domijan2015 uses utils.resolution for all resolving ([`c5b6635`](https://github.com/computational-psychology/stimupy/commit/c5b6635ec13a6d7bc05867667b296a8e05dfe4f8))

* Test that resized stim are within 1 pixels (if ppd not integer multiple) ([`af47865`](https://github.com/computational-psychology/stimupy/commit/af478655b2f527f8095d3e76c3fb16bf75dbd721))

* Use defined visual_sizes, rather than recalculate ([`39b67af`](https://github.com/computational-psychology/stimupy/commit/39b67afb9c4ecb784f5c6bc982b4c4b3c4f3a65c))

* Import and use resolution

not just resolution.resolve ([`449fc8f`](https://github.com/computational-psychology/stimupy/commit/449fc8f54f2ea50f59dbe2253ac1f88afa6e112f))

* Parametrize test for various ppds -- not passing! ([`3bb841f`](https://github.com/computational-psychology/stimupy/commit/3bb841f97917d7a8a7388e78a2fe029cb9ecd01e))

* Test Domijan2015 resizing; integer scaling of ppd ([`e80ee72`](https://github.com/computational-psychology/stimupy/commit/e80ee72d3750abfb297beb1d4796b638248f68cf))

* Bugfix: domiijan2015.checkerboard_contrast_contrast original_shape

with padding is (100,200), not (100,180) ([`4e6dfa5`](https://github.com/computational-psychology/stimupy/commit/4e6dfa538bf7391bdda8cd9db50f79d38f6cb11a))

* Merge branch `feat_utils` into main ([`2482da3`](https://github.com/computational-psychology/stimupy/commit/2482da30b6ccb9e31734c5ed48b0a4022fe47d4d))

* Fix imports now that utils have been split up

Closes #8 ([`8db9a74`](https://github.com/computational-psychology/stimupy/commit/8db9a74a6c88a87d7662e5b85fad164de183f895))

* Degrees to pixels and compute ppd to resolution ([`ed788aa`](https://github.com/computational-psychology/stimupy/commit/ed788aab82d715c7c7b61048f1964fef648e9ef6))

* Move more drawing-like utils to components ([`93b5520`](https://github.com/computational-psychology/stimupy/commit/93b5520295edcd28a50b37b12406b3f1a87bd53e))

* Separate utils for filtering ([`35c6fa5`](https://github.com/computational-psychology/stimupy/commit/35c6fa54edb596a0165f93af1bf3bf4ff2991108))

* Extract plotting to utils.plotting ([`dd03ea0`](https://github.com/computational-psychology/stimupy/commit/dd03ea07dab4779ed26a252b369aba881b1c5d33))

* Move write_array_to_image to utils.export ([`bf7e670`](https://github.com/computational-psychology/stimupy/commit/bf7e67052d430bab427da70fd27e08c39dbc21f5))

* Extract utils for munsell &lt;-&gt; luminance to color_conversions ([`e0ab826`](https://github.com/computational-psychology/stimupy/commit/e0ab826b6bd75c2e5f4aeecbbe9ea4bf2f4601ba))

* Deprecate pixels_to_degrees

in favor of resolution.visual_size_from_shape_ppd ([`39e22ca`](https://github.com/computational-psychology/stimupy/commit/39e22ca22c88e9ab35b7f14e0813e164fb66ff35))

* Deprecate center_array ([`736502b`](https://github.com/computational-psychology/stimupy/commit/736502b31d6568cdbb663f1430bb426d8efbbfd8))

* Use pad_to_visual_size where possible ([`0ab7cc7`](https://github.com/computational-psychology/stimupy/commit/0ab7cc7e0b69c0a90067edcb20ea179afec200d9))

* pad_to_visual_size ([`f929ce9`](https://github.com/computational-psychology/stimupy/commit/f929ce90fb4528350970b1117035da8f493bd7ef))

* pad_by_visual_size ([`f0aeae7`](https://github.com/computational-psychology/stimupy/commit/f0aeae7ebc2ec5383c1ca33950145448b8032b62))

* pad_to_shape ([`bd9fd7d`](https://github.com/computational-psychology/stimupy/commit/bd9fd7dd3046c5e58cdefb0a6e1207f6f8537a4f))

* Tests for pad_by_shape ([`a348153`](https://github.com/computational-psychology/stimupy/commit/a348153eaf55947480ad94995d4d5c8cde39dd0d))

* Rename: pad_array -&gt; pad_by_shape ([`65f60fe`](https://github.com/computational-psychology/stimupy/commit/65f60fe2ea74794c1e588b440099588362d3c956))

* Rename: pad_img -&gt; pad_by_visual_size ([`3037ab4`](https://github.com/computational-psychology/stimupy/commit/3037ab4806f847f50b6ae402c1d7acdc99682f1c))

* All padding functions to separate module ([`79f0dde`](https://github.com/computational-psychology/stimupy/commit/79f0dde0dc780a4c0d7d032f83714a39b1c01575))

* Auto-format ([`ed19e71`](https://github.com/computational-psychology/stimupy/commit/ed19e713b76a0342a53ec6f61a4317d30621c51d))

* made noise code pkg-compatible and added demo JNs ([`2870b6a`](https://github.com/computational-psychology/stimupy/commit/2870b6aa6d3680b94ccf18e30763e74e956c60d1))

* moved illusion demos in subfolder ([`0061392`](https://github.com/computational-psychology/stimupy/commit/006139234b561d06ecd46d27d9e4c1dabcaaa338))

* added circular bullseye (function+demo) ([`ed759d2`](https://github.com/computational-psychology/stimupy/commit/ed759d27519f087f30b5fdcd222d68251521bb03))

* added demo JN for whites ([`3ef39fb`](https://github.com/computational-psychology/stimupy/commit/3ef39fba7667961b41feee5e367bc30786edf975))

* fully fixed misplacement now by only using target thickness // 2 ([`897becb`](https://github.com/computational-psychology/stimupy/commit/897becbeb797059836ffbd6b25e82d1748aaabf4))

* added demo JN for todorovics ([`e1f86ee`](https://github.com/computational-psychology/stimupy/commit/e1f86ee455ab5bc0068c7518c32dbcfd20394d82))

* fixed small bug which led to misplacement of covers ([`83bc31a`](https://github.com/computational-psychology/stimupy/commit/83bc31a8a0642674ac459d138fd51b5c40c6694f))

* fixed bugs in dot-sbcs ([`d4ba075`](https://github.com/computational-psychology/stimupy/commit/d4ba075741209a87f1700a9ac92c32eddb8e10d2))

* added relevant limitation ([`b54eb01`](https://github.com/computational-psychology/stimupy/commit/b54eb01b351e8af3cdf8fe887d6dadd9888ebe56))

* added demo JN sbc ([`a972c88`](https://github.com/computational-psychology/stimupy/commit/a972c880a86980f91f593f700142f17f7c573046))

* added demo JN of hermann ([`8d67b95`](https://github.com/computational-psychology/stimupy/commit/8d67b9582d9e839c8d37cc1e6beb5c12229839b1))

* added demo JN for cornsweet ([`22a90d9`](https://github.com/computational-psychology/stimupy/commit/22a90d9bb7c938889fa80bcd3dcff6e8097c4018))

* added demo JN for circulars ([`18b6a5b`](https://github.com/computational-psychology/stimupy/commit/18b6a5be84833829ae75b4278c916e423323f6ce))

* added demo JN for benarys ([`0717e85`](https://github.com/computational-psychology/stimupy/commit/0717e8562a36e2f8833423d80de343f3dad372c2))

* added more limitations and added two user-friendly todorovic-benary ([`9953c17`](https://github.com/computational-psychology/stimupy/commit/9953c17ccb63e0dacff694afa96990268d5b28a7))

* updated docstrings including reference and use ([`21007d8`](https://github.com/computational-psychology/stimupy/commit/21007d8def579ab89235fcf80bfe74dde8e3647b))

* changed default behavior of domijan-config stims ([`bc81aab`](https://github.com/computational-psychology/stimupy/commit/bc81aab2d2015f1930470a30df1a017cf398cda7))

* updated todorovic params in RHS2007 ([`ebda0ce`](https://github.com/computational-psychology/stimupy/commit/ebda0ce4a5214bab085620bce84b64de901655fc))

* added and updated docstrings ([`743bcf4`](https://github.com/computational-psychology/stimupy/commit/743bcf4c34bd0d22dfd97f6ded93a33b05771f03))

* updated or added scipt-docstrings, and set domijan-default shape and visual_size to None ([`d52e8be`](https://github.com/computational-psychology/stimupy/commit/d52e8be9f32430b1c84e945558a732ce2fd6f5e0))

* Merge branch `dev_refactor` into main ([`6817eb5`](https://github.com/computational-psychology/stimupy/commit/6817eb5cf8643552d0845b5a77a02e7d2d418526))

* consistently use intensity now ([`7fe1884`](https://github.com/computational-psychology/stimupy/commit/7fe18840ed43e42c2ae684926af9a2c42b4bda8e))

* solved merge conflict ([`f30c9a1`](https://github.com/computational-psychology/stimupy/commit/f30c9a1f6a7ef4a11af6e4fd863307973eb594e5))

* renaming some variables more consistently ([`b034d91`](https://github.com/computational-psychology/stimupy/commit/b034d916f0dea299ecbe336ae3f2af87ee6d0275))

* Stub Notebook stimspace for checkerboard ([`f8a980c`](https://github.com/computational-psychology/stimupy/commit/f8a980c43c6063ff3a4755aa74cec271ab964fe1))

* Plot_stim in range (0,1) ([`0eff732`](https://github.com/computational-psychology/stimupy/commit/0eff73292b267affcb8cb5b8e910ff1233d4410d))

* Merge branch `feat_checkerboard` into `dev_refactor`

Checkerboard component and stimuli

See merge request computational-psychology/stimuli!17 ([`b159e70`](https://github.com/computational-psychology/stimupy/commit/b159e701a7bc5c61e9f9491b49d7436ded9755a4))

* Minor docstring stuff ([`fc7e8a8`](https://github.com/computational-psychology/stimupy/commit/fc7e8a85dc1057c200de3ee6505499730be84f60))

* Cleanup ([`94f157e`](https://github.com/computational-psychology/stimupy/commit/94f157ef8ea86c8272038951e41191f52d7b56e5))

* Remove stray import ([`80d1b51`](https://github.com/computational-psychology/stimupy/commit/80d1b51d3321ad244dc0d9319dd9fd34156b201a))

* Clean up imports ([`7688d17`](https://github.com/computational-psychology/stimupy/commit/7688d171b4d42100e0c4390015079507f5c90e3e))

* Update Domijan2015 checkerboard, checkerboard_extended ([`6055a66`](https://github.com/computational-psychology/stimupy/commit/6055a665271347414a95584d3c67eb56dc101b02))

* Murray2020 uses new checkerboard ([`9067bee`](https://github.com/computational-psychology/stimupy/commit/9067bee1c4efd1d6eeb133753fdea76e0d47c681))

* Use new checkerboard illusions for RHS2007 ([`58ef3a2`](https://github.com/computational-psychology/stimupy/commit/58ef3a215d14fe701ba66b66983c095eaae78863))

* Simplify resolving board resolution, and docstrings

..and additional tests ([`fd0f919`](https://github.com/computational-psychology/stimupy/commit/fd0f9195e8e0ea2a02b38a152f023fbf0b38827e))

* Start tests for checkerboard ([`31c4151`](https://github.com/computational-psychology/stimupy/commit/31c4151210663cb2e281a1fc30f3b3d9067205f5))

* Raise error if target(s) fit in board ([`6e898c3`](https://github.com/computational-psychology/stimupy/commit/6e898c3795767add0b72c9238b06a02f143afe58))

* Checkerboard contrast-contrast now also uses new checkerboard ([`ba64cda`](https://github.com/computational-psychology/stimupy/commit/ba64cda1374d7375e3b31a548e8eed3a72281969))

* Remove old checkerboard from components ([`a39cbf5`](https://github.com/computational-psychology/stimupy/commit/a39cbf5523f819d4a97c3a5e3124b88f4882ce3a))

* Use new checkerboard in illusions ([`0022c3a`](https://github.com/computational-psychology/stimupy/commit/0022c3abd54811a307b3dc5c66f10ef4f09a5f53))

* New components.checkerboard module ([`f1d6e91`](https://github.com/computational-psychology/stimupy/commit/f1d6e910c52ebe710e6a0343d8687848e0bb7ca8))

* use reduced mask in murray-white ([`8df0ea2`](https://github.com/computational-psychology/stimupy/commit/8df0ea2cbd09f80dcb16c9ae4245f21b83798995))

* corrected bug in white ([`7f7537a`](https://github.com/computational-psychology/stimupy/commit/7f7537a625ca4225b1d597b253abb19fb3f5f9d5))

* added default visual_size in deg ([`bb4b8ac`](https://github.com/computational-psychology/stimupy/commit/bb4b8acb626ca83518440bcbc38c086971c620db))

* added stim defaults to output dict ([`518c4c7`](https://github.com/computational-psychology/stimupy/commit/518c4c7e9a88661cd6868c2e546f7dc6f01201b1))

* added stim_defaults as params to output dicts ([`6b7e41e`](https://github.com/computational-psychology/stimupy/commit/6b7e41edadd6e20a10e8e92e467d44213f689d91))

* tiny change ([`bf992be`](https://github.com/computational-psychology/stimupy/commit/bf992be99945370ec7c816d63062b2151b5ae838))

* in warnings about shape change, also contain requested shape ([`b95c3af`](https://github.com/computational-psychology/stimupy/commit/b95c3afb52090224aa65d87e711f3104f641feb7))

* only output warning for shape change, if it actually happened ([`60e51d9`](https://github.com/computational-psychology/stimupy/commit/60e51d9fb6494f20f18f401c114c8f9cc1676f07))

* enforcing full period in all white stims to not change the appearance of the stims when changing their size ([`1909708`](https://github.com/computational-psychology/stimupy/commit/1909708706714d1514c3cba96ae179109004cd10))

* removed additional params from json which led to error when generating gts ([`7d8c744`](https://github.com/computational-psychology/stimupy/commit/7d8c744547a7be70495893466be6506e5dc7353e))

* added functionality to pass height and/or width to define stimulus sizes, and added defaults ([`7564806`](https://github.com/computational-psychology/stimupy/commit/7564806a731087aa1ce60cd38c673bc0259cd1b9))

* correct bugs in radial whites and added missing radial white (thin) ([`80660a6`](https://github.com/computational-psychology/stimupy/commit/80660a6c8a09ca234d0a4a094ff240db42f22adb))

* moved targets in todorovic by one pixel ([`a88af96`](https://github.com/computational-psychology/stimupy/commit/a88af96b25437e6306dd15b4fb61a7c048e6f403))

* Merge branch `dev_refactor` of git.tu-berlin.de:computational-psychology/stimuli into dev_refactor ([`d43d5e8`](https://github.com/computational-psychology/stimupy/commit/d43d5e8d8e80477558aa1e6f01b61a42bc1c8ab9))

* updated benarys cross ([`479896d`](https://github.com/computational-psychology/stimupy/commit/479896dc39660147fa76f9632be9cff91c171029))

* Merge branch `feat_resolve_resolutions` into `dev_refactor`

Resolve &amp; validate shape, visual_size, ppd

See merge request computational-psychology/stimuli!16 ([`c9141c0`](https://github.com/computational-psychology/stimupy/commit/c9141c0f09dc6061b32111936675ed50c2d4f43a))

* partially updated benarys cross and changed default ppd for domijan2015 - producing the correct stims ([`31ab942`](https://github.com/computational-psychology/stimupy/commit/31ab942e59088c015b7473aa957c4847eff20452))

* updated sbc variables. added sbc function which automatically centers the target ([`f213016`](https://github.com/computational-psychology/stimupy/commit/f213016ed69b1f0c0a90deb6907377daae55686b))

* updated some variable naming and doc ([`2d13114`](https://github.com/computational-psychology/stimupy/commit/2d13114ddad1b535a82c01de962e870d35cd0e89))

* Bugfix resolve to deal with scalar inputs ([`b181119`](https://github.com/computational-psychology/stimupy/commit/b1811197f33831892eb45e249126fdc410fdfdd0))

* Docstrings ([`19d7056`](https://github.com/computational-psychology/stimupy/commit/19d7056f91b5e21b645b7a16a18261c72f86143f))

* Resolving 2D now resolves each dimension separately ([`2646ed0`](https://github.com/computational-psychology/stimupy/commit/2646ed0a96adc24dd46a071c59f4e98ba4b6fcec))

* Extract 1D resolvers ([`7d13041`](https://github.com/computational-psychology/stimupy/commit/7d1304154a171881cd0a4c06a17b151a23df2152))

* Write (failing) tests for resolve ([`d7d8f90`](https://github.com/computational-psychology/stimupy/commit/d7d8f9084cc3a68166391dabbfecf6d5c12592ef))

* Add tests for canonizing None -&gt; (None,None) ([`fd2fd16`](https://github.com/computational-psychology/stimupy/commit/fd2fd168a62a96359ca38f32bc034b73923ed220))

* Rewrite tests for valid resolutions ([`0823154`](https://github.com/computational-psychology/stimupy/commit/08231545cd17bf0b2d733c1f9fed9596b89910fe))

* Docstrings ([`050d709`](https://github.com/computational-psychology/stimupy/commit/050d70953e46173c3914d20cf0c674c03325edf6))

* PPD does not have to be int ([`fd72297`](https://github.com/computational-psychology/stimupy/commit/fd7229730f395ea7340bb5b57c7637cf3effbdc8))

* Check (&amp; test) for None input(s) ([`cf8f0ed`](https://github.com/computational-psychology/stimupy/commit/cf8f0ed703a94667e4f4db441db5a54e1e378a54))

* Refactor resolving calculations ([`900f840`](https://github.com/computational-psychology/stimupy/commit/900f8400bb6cc4417a0c830b6080ebee6aa71442))

* Warn user about rounding when determining Shape ([`d1b6b40`](https://github.com/computational-psychology/stimupy/commit/d1b6b40d13a2a30f3d9896303a9324423eb591fc))

* Rename to stimuli.utils.resolution ([`165e09b`](https://github.com/computational-psychology/stimupy/commit/165e09b9cc0f0f2dbf9b43a968d256f64a579b4c))

* Function for resolve resolution from 2 knowns ([`683c6ff`](https://github.com/computational-psychology/stimupy/commit/683c6ff4858edae5b10ed6cca142674752d28977))

* Function (w/ tests) for checking that resolution specification is valid ([`5a58a2f`](https://github.com/computational-psychology/stimupy/commit/5a58a2f9ee9972e0e8d26b90e973577656798c1f))

* Function &amp; unittest for getting visual_size from shape and ppd

And mostly use the same tests for all resolvings ([`373752e`](https://github.com/computational-psychology/stimupy/commit/373752eda8e2a814deb27152485696303b1dd6f4))

* Function &amp; unittest for getting shape from visual_size and ppd ([`5f13ea4`](https://github.com/computational-psychology/stimupy/commit/5f13ea44dbc3e5b95b8a9e48aa5550316b48344a))

* Flip width / height -- to be in line with numpy.array.shape ([`03c1648`](https://github.com/computational-psychology/stimupy/commit/03c164882ebfc97b32d1cdf5beee744ae0f4c73c))

* Function and unittest for calculating ppd from shape and visual_size ([`089b6e4`](https://github.com/computational-psychology/stimupy/commit/089b6e479d5a9f4e3734b4236e9e48c3cdaf7779))

* Module for validating shape, visual_size and ppd. Includes tests. ([`d4df484`](https://github.com/computational-psychology/stimupy/commit/d4df484b48925dff0e7ec2dc39b8e2186d098a63))

* Autoformat utils ([`5849fb7`](https://github.com/computational-psychology/stimupy/commit/5849fb775651819cab2cf8227940d0869f7a1109))

* Murray2020.white uses new white_two_rows ([`9613b6c`](https://github.com/computational-psychology/stimupy/commit/9613b6c9a1bcfb750810086869840a7ac5803363))

* All Murray2020 masks should be of dtype int ([`740f12f`](https://github.com/computational-psychology/stimupy/commit/740f12f894d6f0415187dc0503d10bb0269203d5))

* Merge branch `dev_refactor` of git.tu-berlin.de:computational-psychology/stimuli into dev_refactor ([`247b2b2`](https://github.com/computational-psychology/stimupy/commit/247b2b2b14391cb7fb472242befc6604fd8f71ca))

* adapted paper scripts and updated rhs.json because most stims changed by a tiny amount (1 row/col of pixels) ([`f7e7ea1`](https://github.com/computational-psychology/stimupy/commit/f7e7ea1de4411fee7c8d04d0c900a034e1cb53da))

* updated init because of new modules aka moved functions ([`f9bd8d2`](https://github.com/computational-psychology/stimupy/commit/f9bd8d2d1d54e9d96d7549454e08654467ed2696))

* moved wedding cake. still wip ([`56a4747`](https://github.com/computational-psychology/stimupy/commit/56a47470eb8b61ecd746ac63eea91462b06e7bca))

* moved and improved circular white and radial white ([`3da0ec5`](https://github.com/computational-psychology/stimupy/commit/3da0ec505b1d7cf036476d73f35120f55be3fdf2))

* improved existing white functions, made them consistent and added some user-friendly versions. removed circular functions and wedding cake ([`0449e12`](https://github.com/computational-psychology/stimupy/commit/0449e126b15559d72d9ff6f345f4bcb70be8e49b))

* updated old, flexible todo-functions and added user-friendlier versions ([`a886dae`](https://github.com/computational-psychology/stimupy/commit/a886dae689b0f1933c99170b96b2c45d690e2647))

* updated square-wave ([`a035402`](https://github.com/computational-psychology/stimupy/commit/a035402c90083e1a6a1262fafb884785945b6978))

* updated components while updating individual stimuli ([`4b8b6b3`](https://github.com/computational-psychology/stimupy/commit/4b8b6b3a7267c26c57dd199faf4248ce6467fbe2))

* Install matfile for murray2020 stimuli

include it in MANIFEST.in
Closes #28 ([`8014e7b`](https://github.com/computational-psychology/stimupy/commit/8014e7bf35c99708d79b716b8c6194490b27a78b))

* corrected target mask in murray-checkassim and updated docstring ([`4e5b030`](https://github.com/computational-psychology/stimupy/commit/4e5b030bbb7a564d21947f9f1c2c336faaa45706))

* short-term fix for domijan-benary at ppd=48 ([`7e94068`](https://github.com/computational-psychology/stimupy/commit/7e940687377247b7a7682f42afb1bc38a9cab968))

* by default, turn off smoothing in stims ([`37d47e3`](https://github.com/computational-psychology/stimupy/commit/37d47e3b66faf9aa8533dcb4a2ee592a5b3bdfbd))

* made circular stimuli smoother ([`05dec90`](https://github.com/computational-psychology/stimupy/commit/05dec90b973564b452ff1fe689f62e0ef3605c8a))

* added disc_and_rings to components and made it stim-pkg compatible ([`190256f`](https://github.com/computational-psychology/stimupy/commit/190256fa8906d5cdb6a379af83324dfd272a459b))

* murray2020-checkassim created with stim-pkg now (possibility to create without padding added) ([`4c12d75`](https://github.com/computational-psychology/stimupy/commit/4c12d757a4f53ee37788be9b27722acd01dc888c))

* removed hack for aligning benary at ppd=32, height_deg=16 ([`5e5eb13`](https://github.com/computational-psychology/stimupy/commit/5e5eb138f0c52427462c255ab38e10ae593c94d8))

* added a small number to benarys cross target size and 2nd x-coord to make sure that it is aligned at ppd=32 ([`59af60f`](https://github.com/computational-psychology/stimupy/commit/59af60f6afa21029bb55057694b2c90eac64b56b))

* adapted post-rotation treatment of triangles to ensure straight lines in benarys cross ([`e8abeaf`](https://github.com/computational-psychology/stimupy/commit/e8abeafe5dcd77938837ef97e2e7087d1ff7f06a))

* fixed problem that target masks were not exactly the same as target in wheel_of_fortune ([`4437ea2`](https://github.com/computational-psychology/stimupy/commit/4437ea2c3393238a7af651a18254825dd8d9fcf2))

* solved local merge conflict (my mistake) ([`d2aba4f`](https://github.com/computational-psychology/stimupy/commit/d2aba4fc68679781dfcdb6c7389f02ac1c928d58))

* normalized murray2020 stims between 0-1 ([`3f19a7c`](https://github.com/computational-psychology/stimupy/commit/3f19a7c7ca25a1735395c7b1dd574b4c7edbaa27))

* Update checksums for Robinson et al. (2007) stimuli ([`cd1ee08`](https://github.com/computational-psychology/stimupy/commit/cd1ee08e6c8d5a28d7b45d72e454946e2af00b35))

* Update checksums for Domijan (2015) stimuli ([`d7d470c`](https://github.com/computational-psychology/stimupy/commit/d7d470c12f4069e8b8cd7b25fb5ab662b362d91c))

* Normalize all Murray (2020) stimuli to range [0, 1], and test ([`e820c14`](https://github.com/computational-psychology/stimupy/commit/e820c146d7622703c192d1a5ebadfb26d57a46a4))

* normalized stimuli between 0-1 and added original_range ([`2d4e247`](https://github.com/computational-psychology/stimupy/commit/2d4e247d56a0c2ff7dbf0b997fd7996f297baadd))

* removed padding from bullseyes ([`22e28ea`](https://github.com/computational-psychology/stimupy/commit/22e28ea70db35d808c828f07f4e3c8da615e8db7))

* fixed problem that padding wasn't removed in RHS2007-todorovic_in_small ([`ad1f88c`](https://github.com/computational-psychology/stimupy/commit/ad1f88cc9a9958fb8f8bd0d17162aa47ffccbcc8))

* Merge branch `dev_refactor` of git.tu-berlin.de:computational-psychology/stimuli into dev_refactor ([`ba1f0a2`](https://github.com/computational-psychology/stimupy/commit/ba1f0a23ba37037dfc11bc9d34b3818340b24b61))

* made padding optional and added height_px and height_deg as input options ([`8832be7`](https://github.com/computational-psychology/stimupy/commit/8832be7e03470531acd52cc182e41d249e4b9291))

* RHS2007 padding optional ([`fabf701`](https://github.com/computational-psychology/stimupy/commit/fabf701a4bbceccebb62b75dc158491b0d9a15aa))

* Merge branch `lynn_dev` into dev_refactor

Closes #4
Closes #20
Closes #19
Closes #18 ([`c465f3b`](https://github.com/computational-psychology/stimupy/commit/c465f3ba6f72c5c708387f9b2102deda9d32427f))

* added target masks to dotted sbcs ([`de0f7d7`](https://github.com/computational-psychology/stimupy/commit/de0f7d7d1b23be5c739ac93d0665b583c5d15a75))

* corrected docstrings ([`28cf3ae`](https://github.com/computational-psychology/stimupy/commit/28cf3ae01fe0b4f1fe2a10f7e1046f98b4a1075d))

* added grating_uniform, grating_grating and grating_grating_shifted ([`f20a1f9`](https://github.com/computational-psychology/stimupy/commit/f20a1f9897cd28887be5cc09918dc47ba0ee44e6))

* updated use of grating_illusion ([`7f692cf`](https://github.com/computational-psychology/stimupy/commit/7f692cf85f447ac640f3ad6bc326f6f021f59138))

* updated docstring ([`55fd960`](https://github.com/computational-psychology/stimupy/commit/55fd96004278965c07364144587700d01eab68d2))

* using square-wave component now, and changed inputs ([`bcf1ae0`](https://github.com/computational-psychology/stimupy/commit/bcf1ae034a91898e9d44850a8289855ecd0eee48))

* added square-wave component ([`eabe33e`](https://github.com/computational-psychology/stimupy/commit/eabe33e26c5add31c0baae5a18522a8fbbccf5f7))

* added sbc_with_dots and dotted_sbc ([`61ce0ff`](https://github.com/computational-psychology/stimupy/commit/61ce0ff35d57af15a7e51ad47fbaafc404934c45))

* added disc component ([`f62d8ab`](https://github.com/computational-psychology/stimupy/commit/f62d8ab3d8ddbad835ce2debe7078bd2f18ef5cb))

* corrected docstring of rectangle ([`5ff8b64`](https://github.com/computational-psychology/stimupy/commit/5ff8b644fad577299776936d5f4b6d4c5744db07))

* improved sizing of white_zigzag ([`586658f`](https://github.com/computational-psychology/stimupy/commit/586658f7475d499e9641fad4afd8332ec8898127))

* updated paper scripts to function changes ([`985549c`](https://github.com/computational-psychology/stimupy/commit/985549c6afd9b818695ddbe92d421871d010ade2))

* removed padding+doubling ([`e45aa4d`](https://github.com/computational-psychology/stimupy/commit/e45aa4d2f4d901a01fd1cd7c13ae64fc36e058b2))

* cleaned script and adapted docstring ([`902fc34`](https://github.com/computational-psychology/stimupy/commit/902fc34b740c01204e774849f90ff445d0b1cb34))

* adapted herman grid to repo-use ([`f4f6e49`](https://github.com/computational-psychology/stimupy/commit/f4f6e490799b20345645e6e9ea0d7360f18f57a7))

* put checkerboards in one script and removed padding+doubling from functions ([`042dae1`](https://github.com/computational-psychology/stimupy/commit/042dae131435e3ece8adbd2e890e8d8e8138af2a))

* added checkerboard component ([`938faaf`](https://github.com/computational-psychology/stimupy/commit/938faaff10bc3967a499c61409c0bebcc8ef25c2))

* Remove defunct demo scripts ([`1dad027`](https://github.com/computational-psychology/stimupy/commit/1dad027d3bb9bfebc4e0839378993aa2737ada46))

* Merge branch `feat_murray2020` into dev_refactor ([`7da2907`](https://github.com/computational-psychology/stimupy/commit/7da29074a55a877a3a887048996f4c1ec33695a6))

* Remove other implementations of Koffka Ring ([`2c9af41`](https://github.com/computational-psychology/stimupy/commit/2c9af41536cc13217914b3e0e7c266865dfd6a2e))

* Move square_wave to components ([`861ce5e`](https://github.com/computational-psychology/stimupy/commit/861ce5ed5869b7b63de5a6d5e452d1b216f88692))

* Fix some conditionals ([`4cf7e74`](https://github.com/computational-psychology/stimupy/commit/4cf7e7455977fc0e7c5ad187796b7f1e592eec84))

* Fix some imports ([`4a12a62`](https://github.com/computational-psychology/stimupy/commit/4a12a62211793c9c6131b64fadc2bbdcb824d454))

* Murray2020 stimuli take ppd argument

Original PPD = 16 pix / 8 deg
new argument scales this, so only works for even numbers ([`689ee84`](https://github.com/computational-psychology/stimupy/commit/689ee84591a557b6f1afa5d9e8cd59d633bb07d0))

* Merge remote-tracking branch `tubgitlab/noise` into dev_refactor ([`008860d`](https://github.com/computational-psychology/stimupy/commit/008860d06fb29fd647c3bbd7d814443fd0f7774c))

* Dungeon illusion no longer does doubling+padding ([`31a0fc4`](https://github.com/computational-psychology/stimupy/commit/31a0fc457395250041961d141974ef2e07a4a4f8))

* Update checksums for new, and for improved, stimuli ([`e4e6f26`](https://github.com/computational-psychology/stimupy/commit/e4e6f265b7ad09e07bf1e52b9dc2c25bd24d948f))

* Merge remote-tracking branch `tubgitlab/lynn_illusions` into dev_refactor ([`d518f6e`](https://github.com/computational-psychology/stimupy/commit/d518f6ebad0ca9ad98fc819821f86efc8d0c1873))

* Merge branch `feat_testing` into dev_refactor ([`72278d4`](https://github.com/computational-psychology/stimupy/commit/72278d42e91a3e492222d05f0ddfb88b89e7925d))

* Merge branch `feat_plotting` into dev_refactor ([`975c8bf`](https://github.com/computational-psychology/stimupy/commit/975c8bf1ae959277c3f2e70a944d18508233162a))

* gen_ground_truth uses .gen_all() functions ([`653b36a`](https://github.com/computational-psychology/stimupy/commit/653b36a83d25c53e482246c0b1a058f38e65da6c))

* Add .gen_all() function to each paper ([`b101dea`](https://github.com/computational-psychology/stimupy/commit/b101dea0f07772c82de442462658b350a5409d78))

* Extract hashing, saving to JSON as `utils.export` module ([`b622cae`](https://github.com/computational-psychology/stimupy/commit/b622cae9155bfa4911ce9cad858644cbe43ea768))

* target indices (0,0) always indicate the center in zigzag white now ([`cb34a8e`](https://github.com/computational-psychology/stimupy/commit/cb34a8e2873160ada5bf30a5888fe061927f9bde))

* Use md5 hashing, faster than SHA1 ([`611a1bf`](https://github.com/computational-psychology/stimupy/commit/611a1bfbcaef165c77064effdc952ce60ce7ed6d))

* Remove pickles ([`6787d40`](https://github.com/computational-psychology/stimupy/commit/6787d401d0f9c079598450383cb96f0ceced93a1))

* `papers`-module exposes list of papers as __all__

Can now do &#34;from stimuli.papers import *&#34; and get toplevel names &#34;RHS2007&#34;, &#34;domijan2015&#34;, &#34;murray2020&#34;...
so that stimuli can be called by e.g. `RHS2007.WE_thick()`

Can also access this list as stimuli.papers.__all__, which can be used for testing ([`3c60953`](https://github.com/computational-psychology/stimupy/commit/3c60953c4e6f1a07d1824d4381dbe30a4f556fc6))

* added white_zigzag ([`ea0375b`](https://github.com/computational-psychology/stimupy/commit/ea0375b8c06e6f53f051c8f5508e4264cf1d25fa))

* switched input variables of mondrians ([`b2b0f0e`](https://github.com/computational-psychology/stimupy/commit/b2b0f0e8445242af0de67d048138d36a118b2e40))

* added docstring and switched inpt variables ([`26d9176`](https://github.com/computational-psychology/stimupy/commit/26d9176256623ea6d5b030ec29f1f333cf639f47))

* updated and added docstring ([`a2b8109`](https://github.com/computational-psychology/stimupy/commit/a2b8109fc5fb9a3b127f2a7ef1b39b11b7e59970))

* removed matplotlib import ([`a1cb861`](https://github.com/computational-psychology/stimupy/commit/a1cb861c9c44b3a5c9d939a53537d49969a7ffc3))

* added corrugated mondrians ([`25cbc30`](https://github.com/computational-psychology/stimupy/commit/25cbc30b621947d1847e9882244e33fef4d44cd4))

* parallelogram: allow both directions ([`969d959`](https://github.com/computational-psychology/stimupy/commit/969d9593175ebd2239032f69e0114c9766f81073))

* added parallelogram ([`28c3884`](https://github.com/computational-psychology/stimupy/commit/28c388404a6ba484d11a4925e372b2c78a538d7c))

* removed old todorovic function ([`dc2bf7f`](https://github.com/computational-psychology/stimupy/commit/dc2bf7f135b7d6c617cf416565a6c22caba3ba25))

* removed old sbc function and added docstring ([`42ca612`](https://github.com/computational-psychology/stimupy/commit/42ca6121fee819abd7900cf4380cbb871e0ac4ad))

* updated paper scripts to work with updated functions and added more missing stimuli ([`5b71618`](https://github.com/computational-psychology/stimupy/commit/5b71618584ebc9d9db933d9485b7807e982c7f91))

* created single functions for sbc and todorovic stimuli and changed functionality ([`a2e0cac`](https://github.com/computational-psychology/stimupy/commit/a2e0cac3e26c35c697b01778a46a13b7bf10503a))

* removed old rings, changed name and small updates ([`46b50f6`](https://github.com/computational-psychology/stimupy/commit/46b50f6437ea16cad19cb9733663fecb7efea626))

* removed old bullseye, changed name and small updates ([`e6debd3`](https://github.com/computational-psychology/stimupy/commit/e6debd3105739792b227f01a52796e9016c8aff9))

* renamed rings and bullseye ([`a219b6b`](https://github.com/computational-psychology/stimupy/commit/a219b6b657f18b83cb30b80983a9d5606e006227))

* added component rectangle and some docstrings ([`fc4be09`](https://github.com/computational-psychology/stimupy/commit/fc4be09b65a28cbda7f234b8cc8be5b8e45c8528))

* small correction ([`8090373`](https://github.com/computational-psychology/stimupy/commit/809037358e6afaa6dd94597d10d4585c5c2866ef))

* removed old bullseye, changed illusion name and doc ([`cd32421`](https://github.com/computational-psychology/stimupy/commit/cd3242191f1ae129792874f1e98e4fa63531f9bd))

* created component cross and replaced code in benary ([`5442e3e`](https://github.com/computational-psychology/stimupy/commit/5442e3e0afe91711751a5623630cd4ae77a7921e))

* tiny update in error msg ([`a4f5b36`](https://github.com/computational-psychology/stimupy/commit/a4f5b3678eb85876afb35455591be5106cfcb7c7))

* updated anderson white and added yazdanbakhshs white; added missing stimuli for domijan2015 (white yaz, white and, white how) ([`fd47264`](https://github.com/computational-psychology/stimupy/commit/fd47264c8d59d9f491c4cde2f69bc819d2afba91))

* Reduce gen_ground_truth to single (flexible) function ([`260eeef`](https://github.com/computational-psychology/stimupy/commit/260eeef97fb9798169b9a79b7987e9b6bdfda0a9))

* Use hashes of img, mask, in testing ([`e572053`](https://github.com/computational-psychology/stimupy/commit/e572053da46294933bd6b7a0bb2683ddae057312))

* updated benarys cross to allow more targets and also triangular targets; added benarys to rhs2007 ([`811252a`](https://github.com/computational-psychology/stimupy/commit/811252a287e0dc32670929a5c1e7655f206b9c6d))

* added components, added triangle function ([`2e9c08d`](https://github.com/computational-psychology/stimupy/commit/2e9c08ddc0e77de0253b1599d37d88fb499ea39a))

* updated rings and bullseye to only create single stim and let paper-pys do the stacking and padding ([`7314b85`](https://github.com/computational-psychology/stimupy/commit/7314b85e480e350a47cf9b7719404e93ace1bcbd))

* added titles to plotting function and changed cmap for target masks ([`0c2f395`](https://github.com/computational-psychology/stimupy/commit/0c2f395b36ba90977d3f5704a327da527cc0a7d7))

* Murray2020 uses plot_stims ([`284c385`](https://github.com/computational-psychology/stimupy/commit/284c38564a8a1b4d942b1e5968f771e65b1e0742))

* Make masks=false default when plotting paper stims ([`a8b4433`](https://github.com/computational-psychology/stimupy/commit/a8b4433bae7b7fe2c529fbfb59e0b33244809f6b))

* plot_stims takes argument for showing masks ([`fceaa47`](https://github.com/computational-psychology/stimupy/commit/fceaa4763df1eaaf13fbbe542b46bac2032abe93))

* Unify plot_stim usage ([`231c9ba`](https://github.com/computational-psychology/stimupy/commit/231c9ba47723e2170257d1b2d8d3d291f198686c))

* Merge remote-tracking branch `tubgitlab/lynn_illusions` into dev_refactor

Mainly auto-formatting, but also use utils.plot_stim ([`f1c716a`](https://github.com/computational-psychology/stimupy/commit/f1c716a9953568e473158413b740540919408a1c))

* Padding mostly done by paper functions

For some &#34;double&#34; stimuli, it's still done inside the stimulus function itself... ([`874a014`](https://github.com/computational-psychology/stimupy/commit/874a0146c05a86a31b5ce7e7d4492a12da83f2ef))

* Autoformat utils ([`b739247`](https://github.com/computational-psychology/stimupy/commit/b7392476eab9b2ce358675bc615b5deafb5d2684))

* adapted cornsweet illusion and added mask ([`821263d`](https://github.com/computational-psychology/stimupy/commit/821263d53458fbc85b6bc47184e57e3f17dcb254))

* Robinson et al (2007) stimuli generated by papers/RHS2007 ([`da4f0d2`](https://github.com/computational-psychology/stimupy/commit/da4f0d249ccf3469b538f4d57dd1c6d40a0f450b))

* added lynns noise code ([`0a64108`](https://github.com/computational-psychology/stimupy/commit/0a641085628256ab1759241fe95c8abf3a8c54a6))

* Remove Stimulus.Stimulus ([`1110ca6`](https://github.com/computational-psychology/stimupy/commit/1110ca69ca76c832ff5b66150a835e3a2516b187))

* Autoformat ([`f1b0e05`](https://github.com/computational-psychology/stimupy/commit/f1b0e051cf7d01d15f7f84f729123b375ae76440))

* Domijan (2015) stimuli generating in papers/domijan2015 ([`8e49d99`](https://github.com/computational-psychology/stimupy/commit/8e49d990655069b85eaf9bbc81a8125678dfce61))

* Murray2020 in papers/__init__ ([`c9d16fe`](https://github.com/computational-psychology/stimupy/commit/c9d16fe962ffc3ca60d61bf664b7fd55828bb1e8))

* Remove vestigials ([`303f720`](https://github.com/computational-psychology/stimupy/commit/303f720a790775fca3550b09cfc6babece5dd3c9))

* Regression test Domijan2015 against pickled output ([`bde86be`](https://github.com/computational-psychology/stimupy/commit/bde86be0ace5abb29abc2cb475db9b804639fa78))

* Pickle output Domijan2015 ([`8a4c96d`](https://github.com/computational-psychology/stimupy/commit/8a4c96d2164276432197e264123a3a99454b5707))

* Update Domijan2015 tests ([`942476d`](https://github.com/computational-psychology/stimupy/commit/942476d6fc88af66ec03871c2d23dfe372eeecca))

* Bring Domijan2015 in line with other papers ([`5eef7aa`](https://github.com/computational-psychology/stimupy/commit/5eef7aa467c43a5edf55f554b4fb6ece6b2e6e79))

* Clean up RHS2007 plotting code a bit ([`ea466cb`](https://github.com/computational-psychology/stimupy/commit/ea466cb7e7711b70277568815803f123bed51aa6))

* NotImplement RHS2007 raise errors ([`ab5d943`](https://github.com/computational-psychology/stimupy/commit/ab5d943e5066ddcafa7671d691f541fbd970a083))

* Export all RHS2007 stimuli explicitly ([`36b787b`](https://github.com/computational-psychology/stimupy/commit/36b787b0834c0460cca3af38419436c6ccffea59))

* Merge branch `murray2020` into `main`

Murray (2020)  stimuli

See merge request computational-psychology/stimuli!14 ([`1387f2c`](https://github.com/computational-psychology/stimupy/commit/1387f2c545f5ec8d10d1f9e26cfd9838ebdea9db))

* Add note about Haze illusion to module docstring ([`e558bdd`](https://github.com/computational-psychology/stimupy/commit/e558bdd5c7d27775295a7b120f7d57e91d141d03))

* More flexible plotting ([`313e9b3`](https://github.com/computational-psychology/stimupy/commit/313e9b36511d78120266b1fa66e3ed9b4d81fec0))

* Fix argyle masks ([`a8192ea`](https://github.com/computational-psychology/stimupy/commit/a8192eac2be63534c841999bf52ea7f1b90afca8))

* Docstrings for each function ([`378b1e2`](https://github.com/computational-psychology/stimupy/commit/378b1e201de533c9a625d48f3bbaca599827d27e))

* Bugfix: import math ([`577eaf0`](https://github.com/computational-psychology/stimupy/commit/577eaf0bdb83375ea90aa5977e0a23b57c0cb056))

* Module level docstring ([`8cf46ea`](https://github.com/computational-psychology/stimupy/commit/8cf46ea8e74d5966671c17f9eb5da0276df8a329))

* Softcode stimuli testing ([`a8dee47`](https://github.com/computational-psychology/stimupy/commit/a8dee473feaf4a545b45b09c5030af9ce58e8155))

* Explicitly export only stimuli from Murray2020 ([`c07e735`](https://github.com/computational-psychology/stimupy/commit/c07e73576221731f2bf6ad1044f7f08f276b4aec))

* Set up tests for murray2020 stimuli ([`a810784`](https://github.com/computational-psychology/stimupy/commit/a810784a3029bd214e4dfaf2529cda3a26a063d6))

* Don't print matfile filename ([`d9f81bb`](https://github.com/computational-psychology/stimupy/commit/d9f81bb822d365810532ab43d4e3e8f26fe562a9))

* Cleaner masks ([`8c608fa`](https://github.com/computational-psychology/stimupy/commit/8c608fab8486a4699dbd09360f28160abd6c6eef))

* Cleaner way of getting masks ([`b3d5e4a`](https://github.com/computational-psychology/stimupy/commit/b3d5e4a60448251f8a65717eaee00ea68a66b168))

* Fix argyle masks ([`cc8c2a5`](https://github.com/computational-psychology/stimupy/commit/cc8c2a5f4b43a356e0ab624e67bbe957fa13b865))

* Bit of cleaning ([`50092f5`](https://github.com/computational-psychology/stimupy/commit/50092f5c279e489f57e47bd01904de3ac18ed8e2))

* Remove ini_matrix

Use np.zeros instead ([`a83b8f4`](https://github.com/computational-psychology/stimupy/commit/a83b8f47b739ff985d4770891cac4a18c9d79a1b))

* Combine into single module papers/murray2020 ([`566e55f`](https://github.com/computational-psychology/stimupy/commit/566e55fdcd08042913876c304c052905c86d1610))

* Delete murray2020_script.py ([`782b841`](https://github.com/computational-psychology/stimupy/commit/782b841525e808c760c7b401d53e7f1934f0cb9b))

* all stimuli and masks from the murray2020 paper ([`0cc2ff5`](https://github.com/computational-psychology/stimupy/commit/0cc2ff560f9826aebad5fabb42e83fc1d54679f0))

* final version ([`54ef53b`](https://github.com/computational-psychology/stimupy/commit/54ef53b40ff341e1c77e235bbbb489c1fad7b898))

* Delete murray2020.py ([`a0f9f2a`](https://github.com/computational-psychology/stimupy/commit/a0f9f2a3a819bff625e917eee98ce91897a94e9d))

* Murray2020 demo script to plot stimuli and masks ([`fae3526`](https://github.com/computational-psychology/stimupy/commit/fae3526c6ef954be8ac904688c9944c8bc569959))

* returns stimulus + mask as a dict ([`3b077d0`](https://github.com/computational-psychology/stimupy/commit/3b077d04f4ef1ae709b8f74857bef8adcf480dc6))

* creates koffka connected automatically and returns the stimulus and mask ([`448dab8`](https://github.com/computational-psychology/stimupy/commit/448dab8d688ee69e3111970369573a7dcb3241ac))

* creates koffka adelson automatically for different ppd and returns the stimulus and mask ([`3e0dc84`](https://github.com/computational-psychology/stimupy/commit/3e0dc846421a539b50b969c2865825fffa3fb358))

* first version of plotting all stimuli and masks ([`ebfb7ef`](https://github.com/computational-psychology/stimupy/commit/ebfb7ef04e84eabc9e5129358846414f5828ca02))

* Revert &#34;Add new file&#34;

This reverts commit 7a1d86437871fb893c9d10534675bef45b08e64d. ([`f753712`](https://github.com/computational-psychology/stimupy/commit/f753712514b0c3f56c4ac6ab45184cd924f880bd))

* Parameterized Adelson's Koffka ring ([`26f2672`](https://github.com/computational-psychology/stimupy/commit/26f2672a263c93794cdf1545103b3f243cdda49e))

* Add new file ([`7a1d864`](https://github.com/computational-psychology/stimupy/commit/7a1d86437871fb893c9d10534675bef45b08e64d))

* Update pathfinding for matlab file ([`a1dc2ee`](https://github.com/computational-psychology/stimupy/commit/a1dc2ee9ff679f32993d8d839cbc5862d75487fd))

* Upload New File ([`2792080`](https://github.com/computational-psychology/stimupy/commit/2792080875178956911cdf465df759930c7268a6))

* Murray2020 stimuli script ([`ca5610a`](https://github.com/computational-psychology/stimupy/commit/ca5610a8f4ada6da2286eab528e4d8bba1fa0a16))

* RHS2007 WE_Thick resize and offset targets by 1 pixel to match exactly ([`25ba029`](https://github.com/computational-psychology/stimupy/commit/25ba0294424dae6a1807e1772408396a377034d6))

* changed img from attribute to dict ([`063a1c5`](https://github.com/computational-psychology/stimupy/commit/063a1c5223304057d8ab51186b1f12f9e19b5f1b))

* adapted RHS2007 demo script to using dicts instead of stimuli objects ([`73e6889`](https://github.com/computational-psychology/stimupy/commit/73e688952de0b52455b102d199468086a7cbbdb8))

* corrected padding value for domijan white ([`0e28f39`](https://github.com/computational-psychology/stimupy/commit/0e28f393e5f80a0a4644c490f61f66afc8de9ec2))

* changed target_mask to mask for todorovic ([`0664d20`](https://github.com/computational-psychology/stimupy/commit/0664d20df5276e0baca61927725d9c8e4559a795))

* Bugfix: Todorovic illusions produces dict as output ([`1f198c2`](https://github.com/computational-psychology/stimupy/commit/1f198c20872aa15868d7831838c198a39f5aa950))

* changed the function to take in Michelson contrast as input and to be robust to changes in ppd ([`fb100ca`](https://github.com/computational-psychology/stimupy/commit/fb100ca679384394177c530cacc628ad1ad30e9f))

* fixed output format of one white func ([`32bdfb8`](https://github.com/computational-psychology/stimupy/commit/32bdfb8e9ae66a90cc0a998f9bc37d69a310bf54))

* changed output format from object to a dictionary ([`43bdd90`](https://github.com/computational-psychology/stimupy/commit/43bdd904fd782666fbec06becdd4328b0ce9b315))

* Bugfix: circular White's illusion would have gap between rings ([`0c6c2d1`](https://github.com/computational-psychology/stimupy/commit/0c6c2d1945c87e5e86385fcf9909b6a0f7d17a09))

* Bugfix: circle mask would miss pixels ([`5eada03`](https://github.com/computational-psychology/stimupy/commit/5eada03229c9c3596d7772a92dc8e99d061592de))

* Merge branch `main` of git.tu-berlin.de:computational-psychology/stimuli into main ([`ae92d9c`](https://github.com/computational-psychology/stimupy/commit/ae92d9cefe7705f2113b200d5666b9938a4db4b0))

* corrected weird target placing behavior for uneven SF-resolution combinations ([`d070464`](https://github.com/computational-psychology/stimupy/commit/d07046452c1847614cf80eaaa0dde112f0521c87))

* Bugfix: whites tries to import stimuli which causes problems on Python2 ([`a0a12cc`](https://github.com/computational-psychology/stimupy/commit/a0a12cc3c1772ae13ffcd0811f2c2b713c05213e))

* fixed bug in whites which led to right target being misplaced for certain spatial frequencies ([`af219e6`](https://github.com/computational-psychology/stimupy/commit/af219e62a08f852b83f433ec94a3fee2ea99eb51))

* changed target mask of grating induction to contain two target values (target between black/white bars) ([`a1a0bc1`](https://github.com/computational-psychology/stimupy/commit/a1a0bc15191cc154b9b1b9c16bce0a10b50ca1ea))

* Fix some checkerboard stimuli ([`dc10194`](https://github.com/computational-psychology/stimupy/commit/dc10194cc393b63500a310496f1efb311ff123e1))

* changed functions to create target masks with two target values by default ([`a067ae6`](https://github.com/computational-psychology/stimupy/commit/a067ae623712278cda7ffd59ef487fa6b090bea5))

* Bugfix from merge conflict ([`a527c7d`](https://github.com/computational-psychology/stimupy/commit/a527c7d3dacb4fc5a2a54ac415d23426f017a4c1))

* Merge branch `main` of git.tu-berlin.de:computational-psychology/stimuli ([`4ce80b6`](https://github.com/computational-psychology/stimupy/commit/4ce80b687e0c3078f4b985c17e48a70917aeef19))

* added support for multiple targets ([`8f4dcd9`](https://github.com/computational-psychology/stimupy/commit/8f4dcd901549a63fd5386a00482047ff64cba571))

* fixed some bugs in whites generation and added padding_val param ([`519992c`](https://github.com/computational-psychology/stimupy/commit/519992c8fbb7ac31d79f647fddeb0932d4bca511))

* Fixed typo ([`302366f`](https://github.com/computational-psychology/stimupy/commit/302366f22913eb0351c44366c30e37323aea493d))

* Explicitly provide pad value for each edge ([`56f66ce`](https://github.com/computational-psychology/stimupy/commit/56f66ce8e509b51ed1059a9d8c3184e6b392bda8))

* Make Python2.7 proof

Mainly fixing circular imports, and dividing by floats instead of ints ([`0528281`](https://github.com/computational-psychology/stimupy/commit/0528281ab738421d9568541e24a3317b0626fb3a))

* added all authors in setup.py ([`cdbda26`](https://github.com/computational-psychology/stimupy/commit/cdbda260598e96589aa91fa52d809ad1ae8eb0f6))

* added docstrings and updated READMEs ([`3d47a1d`](https://github.com/computational-psychology/stimupy/commit/3d47a1df98300ac7141f4bcd4bd450dd15e4ebef))

* cleaned up the repo for ECVP ([`e1226ad`](https://github.com/computational-psychology/stimupy/commit/e1226ad25ecf9f68613950ef393225963178e0d1))

* deleted whites_old.py ([`e691725`](https://github.com/computational-psychology/stimupy/commit/e69172562b513557b44cc9c036b63d713a46d001))

* added find_packages in setup.py ([`864599a`](https://github.com/computational-psychology/stimupy/commit/864599aa2280d83e7efcda585af52fe7e664a4c7))

* minor changes in the overview.py ([`7e61cfc`](https://github.com/computational-psychology/stimupy/commit/7e61cfc2de7557155bbf4bd2985e85b2880acce9))

* all functions now call other functions with illusion.* even if they're inside the same file ([`f3c4cda`](https://github.com/computational-psychology/stimupy/commit/f3c4cda4cbc01023b62eece0b57ed8c9fd80d97a))

* deleted lightness dir ([`34e505c`](https://github.com/computational-psychology/stimupy/commit/34e505c72abbce50efa969bfd0d550c3710c51f9))

* Merge branch `stimuli_masks` ([`efd85ac`](https://github.com/computational-psychology/stimupy/commit/efd85acb27ef71012399ed11209344f67cfb1ecc))

* corrected stimulus implementations for domijan2015 and RHS2007 ([`a6d1bcf`](https://github.com/computational-psychology/stimupy/commit/a6d1bcf3aec831806496eb578f4b05f538814cbf))

* added test for checkerboard_contrast_contrast ([`ba96fb5`](https://github.com/computational-psychology/stimupy/commit/ba96fb5774d23fa671b97678593d5dd579e785fb))

* Merge branch `master` of git.tu-berlin.de:computational-psychology/stimuli ([`c3cc62c`](https://github.com/computational-psychology/stimupy/commit/c3cc62c3cdc0c53594be768439d90f13d33600f6))

* added overview.png creation in the papers plots ([`d176d5a`](https://github.com/computational-psychology/stimupy/commit/d176d5afec6e7e71cc85da660405265d247a6414))

* changed padding in some functions so they match the shape in the paper ([`f58e1bd`](https://github.com/computational-psychology/stimupy/commit/f58e1bd7e275854163be52c593020802ceaaf5c5))

* Merge branch `replicating_RHS2007_stimuli` ([`9a0e3c5`](https://github.com/computational-psychology/stimupy/commit/9a0e3c5b3fca9db1980738144e60353af0866968))

* changed starting phase of RHS2007_white_thin_wide ([`e94013e`](https://github.com/computational-psychology/stimupy/commit/e94013e60da9705cf395b0266ac9459f0db76ab1))

* corrected WE_thin_wide to match stimulus in RHS2007 ([`83e3cd5`](https://github.com/computational-psychology/stimupy/commit/83e3cd5b819c13a04758207abf9b948cb5acac60))

* changed plotting of RHS overview ([`4adad81`](https://github.com/computational-psychology/stimupy/commit/4adad81feed20be1002a692888b3df85bf795ed0))

* Fixed binary masks for todorovic, circular and sbc ([`06d291b`](https://github.com/computational-psychology/stimupy/commit/06d291bf395dd95d50928586d10b3f74f95223d8))

* Fixed binary masks for todorovic, circular and sbc ([`1890dfc`](https://github.com/computational-psychology/stimupy/commit/1890dfcc65c4cffc3d3a660a2b011e5ffcd234c9))

* Merge branch `master` into stimuli_masks ([`4d9aa41`](https://github.com/computational-psychology/stimupy/commit/4d9aa4190bd797ea3f887c2016a6ced2bdbcee28))

* Merge branch `replicating_RHS2007_stimuli` into `master`

Replicating rhs2007 stimuli

See merge request computational-psychology/stimuli!12 ([`ad11f9d`](https://github.com/computational-psychology/stimupy/commit/ad11f9d6a51ce71360df3041826fe23bac284bf7))

* Merge branch `master` into replicating_RHS2007_stimuli ([`70a8afa`](https://github.com/computational-psychology/stimupy/commit/70a8afa421be1741d971ed132164fffd1a5c16c8))

* added checkerboards in RHS2007 file ([`ae22229`](https://github.com/computational-psychology/stimupy/commit/ae2222987a5389c37e73aad3204220cc95c5d112))

* Merge branch `master` into stimuli_masks ([`5c835c1`](https://github.com/computational-psychology/stimupy/commit/5c835c101902031a0c7e01385d32582bfacdba3b))

* fixed binary masks for todorovic, sbc an white_circular ([`b09354a`](https://github.com/computational-psychology/stimupy/commit/b09354a79177193550fe67406da2bf5e96a359fd))

* added checkerboards ([`298a289`](https://github.com/computational-psychology/stimupy/commit/298a289eff87368d96202d9ae859e37907ea35db))

* added checkerboards ([`8ee27fe`](https://github.com/computational-psychology/stimupy/commit/8ee27fe737bd19588f56ebca00ecee19fb99b283))

* Merge branch `master` into replicating_RHS2007_stimuli ([`1823e05`](https://github.com/computational-psychology/stimupy/commit/1823e0599da8aa51cd34bece7db92a7a4d2f075f))

* added checkerboards ([`c0e417d`](https://github.com/computational-psychology/stimupy/commit/c0e417d7530ff42bf8c5b351eb22671bd4386eb5))

* Merge branch `stimuli_masks` into `master`

implemented binary masks

See merge request computational-psychology/stimuli!10 ([`8740d53`](https://github.com/computational-psychology/stimupy/commit/8740d53daca3743d1c8e72f044d76506ee2b6ff2))

* implemented binary masks ([`af4eaf2`](https://github.com/computational-psychology/stimupy/commit/af4eaf2111394f497168f01205c85c89c1b7d5de))

* Sensible defaults for disc_and_ring

Borrowed from `lightness` demo script ([`28b060b`](https://github.com/computational-psychology/stimupy/commit/28b060b7fb0f54ef17fd9edbd6310ebb3c9a5f8b))

* Bugfix: disc and ring

Didn't produce output, and wasn't imported in `illusions` ([`dd749e2`](https://github.com/computational-psychology/stimupy/commit/dd749e2f45b7b1d429991cec5832fabaed3e60ba))

* Clean-up tests

Rename scripts that just plot (and don't assert anything) to `demo_`, to avoid being run automatically by pytest.

Include an empty __init__.py in tests to help with pytest discovering tests in `tests/papers/domijna2015/` ([`fa78d16`](https://github.com/computational-psychology/stimupy/commit/fa78d16ac8455a140f5ca06d3a7a7457ab643357))

* Merge branch `replicating_RHS2007_stimuli` into `master`

changed some parameters in circular_whiteRHS2007

See merge request computational-psychology/stimuli!9 ([`24a47c2`](https://github.com/computational-psychology/stimupy/commit/24a47c239b750ab2d6673df5fbc158bbf0e79d0f))

* Merge branch `master` into replicating_RHS2007_stimuli ([`4aa69e6`](https://github.com/computational-psychology/stimupy/commit/4aa69e6b6a9e65215d84c53c23e1b529a64842c1))

* changed some parameters in circular_whiteRHS2007 ([`989e0c7`](https://github.com/computational-psychology/stimupy/commit/989e0c75fbaac4e66cfaf6b595a5d70dc5ded22b))

* Merge branch `replicating_domijan_stimuli` into `master`

added tests to compare with hardcoded domijan stimuli

See merge request computational-psychology/stimuli!8 ([`faafff7`](https://github.com/computational-psychology/stimupy/commit/faafff71e69700e6a03ec58096ad8f679b737fdd))

* added tests to compare with hardcoded domijan stimuli ([`7bcb5ed`](https://github.com/computational-psychology/stimupy/commit/7bcb5edb8e7dec5f71e8bdb23558501d1a5474be))

* Merge branch `restructuring` into `master`

stimuli are specified in degrees visual angle

See merge request computational-psychology/stimuli!7 ([`34e5ca2`](https://github.com/computational-psychology/stimupy/commit/34e5ca24548ee5fd28e8d89b9890f77e21ab62cc))

* added Stimulus class and made all functions return a stimulus object ([`72a9983`](https://github.com/computational-psychology/stimupy/commit/72a998322aa07968046bb4fe8db5a12c29f21b60))

* Merge branch `replicating_RHS2007_stimuli` into `master`

Replicating rhs2007 stimuli

See merge request computational-psychology/stimuli!6 ([`8c36bef`](https://github.com/computational-psychology/stimupy/commit/8c36bef74073ddba65418f8a0f9858171de21126))

* stimuli are specified in degrees visual angle ([`c68b54c`](https://github.com/computational-psychology/stimupy/commit/c68b54c401df3c2acd5f4653e8ee061a34e6fc7b))

* RHD2007 stimuli are mostly replicated ([`4912557`](https://github.com/computational-psychology/stimupy/commit/4912557c9beae0f4b9a97dc394dcbcd3d66e31ce))

* the stimuli for which we already have the functions are correctly parametrized ([`a7d6dd6`](https://github.com/computational-psychology/stimupy/commit/a7d6dd68ef290badd8ce16b276bf5ef1801c7ce3))

* Merge branch `replicating_domijan_stimuli` into `master`

added last three domijan stimuli, all of them are done (for real this time)

See merge request computational-psychology/stimuli!5 ([`8ed3f0d`](https://github.com/computational-psychology/stimupy/commit/8ed3f0d34fdf637842e48768176972618cce72a1))

* added last three domijan stimuli, all of them are done (for real this time) ([`76ca93f`](https://github.com/computational-psychology/stimupy/commit/76ca93f8acdc07a379fbf34675c298f9577952fb))

* Merge branch `replicating_domijan_stimuli` into `master`

domijan stimuli are all perfectly reproduced

See merge request computational-psychology/stimuli!4 ([`c6b5ed2`](https://github.com/computational-psychology/stimupy/commit/c6b5ed211b48d7e566f6b4fa7f8a206ed7e721dd))

* Merge branch `master` into replicating_domijan_stimuli ([`d6b070d`](https://github.com/computational-psychology/stimupy/commit/d6b070dd692405a651dca7cc5e4deb7a811d267a))

* domijan stimuli are all perfectly reproduced ([`39ff3cd`](https://github.com/computational-psychology/stimupy/commit/39ff3cddbf120703178e8411cd68f0b132fa988b))

* Merge branch `matko` into `master`

Recent refactorings

See merge request computational-psychology/stimuli!3 ([`c85afc4`](https://github.com/computational-psychology/stimupy/commit/c85afc40aa5e8b7baa73b941b893e3e57fcdd9fc))

* merged lightness into illusions ([`97f85d4`](https://github.com/computational-psychology/stimupy/commit/97f85d4276cc2cbcb4a4a82296011a34097bc641))

* presenting the pipeline to the lab ([`a920cdd`](https://github.com/computational-psychology/stimupy/commit/a920cdd997e89338c61baa3ad123f671f1f009e5))

* Added RHS2007 in papers_stimuli, WIP ([`1147347`](https://github.com/computational-psychology/stimupy/commit/11473473670b0d8272c684e39c1d41131ac5d2f5))

* Added overview generating scripts in illusions and lightness ([`7e4a8bc`](https://github.com/computational-psychology/stimupy/commit/7e4a8bcd43d9fbc6c3061a6113bf1558c6f97343))

* Merge branch `master` into matko ([`74c69fd`](https://github.com/computational-psychology/stimupy/commit/74c69fd5e74a668975819159bed6c135b67ab19c))

* added domijan2015 functions in stimuli ([`88237e6`](https://github.com/computational-psychology/stimupy/commit/88237e6ee7b3a89b24b7fd929d4ccf189ae1cb57))

* Draft params Todorovic illusions

Not sure which params are descriptive ([`04aa624`](https://github.com/computational-psychology/stimupy/commit/04aa62452941a2a643e564f184da6ec8dbcf75e9))

* Add params checkerboards ([`a8c12a9`](https://github.com/computational-psychology/stimupy/commit/a8c12a9fbfe5856f7e04ad47327da0841db04d31))

* Parameters for RHS 2007 now python script, more fleshed out ([`d45778a`](https://github.com/computational-psychology/stimupy/commit/d45778ae339b0af58fadecb271d5d575596007b6))

* Add draft config JSON for RHS 2007 stimuli ([`dbe07d3`](https://github.com/computational-psychology/stimupy/commit/dbe07d3729c04762f02141a34d5e3726a3e905d6))

* Merge branch `matko` into `master`

Make package pip installable

See merge request computational-psychology/stimuli!2 ([`8eada0a`](https://github.com/computational-psychology/stimupy/commit/8eada0af5df469d78197ae462ab70827a50ffcd4))

* fixed __init__.py files to enable imports when installed as package ([`1d2df0a`](https://github.com/computational-psychology/stimupy/commit/1d2df0a47ea35bcd5231f2dcec04bedf22f8c480))

* Some code formatting ([`571eef9`](https://github.com/computational-psychology/stimupy/commit/571eef9b101acc92c258bd6a24a5c15c5530443f))

* Convenience importer for Domijan 2015 illusions ([`ea55ad7`](https://github.com/computational-psychology/stimupy/commit/ea55ad7818f97324acb700310934b03454daa325))

* import all illusions in illusions init ([`12ab7e7`](https://github.com/computational-psychology/stimupy/commit/12ab7e7d6f0158d75553be566a23d741928ade58))

* Brightness_illusions2.py -&gt; whites.py ([`5a21ca8`](https://github.com/computational-psychology/stimupy/commit/5a21ca83a78035ec1e7363173eaf517bd5d12bbe))

* Separate out individual illusions ([`795223d`](https://github.com/computational-psychology/stimupy/commit/795223d256f8c202b1406a2b38436aead683e099))

* Ignore VSCode settings ([`5d07c13`](https://github.com/computational-psychology/stimupy/commit/5d07c13effd4ec5904d1389eaab9280ebbfc3013))

* Make package pip installable

Rename `src` -&gt; `stimuli`, update setup.py
Now installabe with `pip install .`, and `pip install -e .`, so that dependencies automatically get installed etc.
Updated README ([`9410df2`](https://github.com/computational-psychology/stimupy/commit/9410df274dbfbbad871cdf80290fd073b2c95c5c))

* implemented more stimuli ([`6a63987`](https://github.com/computational-psychology/stimupy/commit/6a639875c7ca35e961bd6f696af6966cfe3546d9))

* implemented flexible functions for some brightness illusions ([`296d3cc`](https://github.com/computational-psychology/stimupy/commit/296d3ccbfaabca27c6e8c8bbbf2da906735c4a45))

* included brightness illusions and cleaned up package ([`0f29746`](https://github.com/computational-psychology/stimupy/commit/0f29746d85e042761620a3bb72fd942802bf477d))

* Merge pull request #1 from computational-psychology/dev_metrics

Adds Moulden's 1990 definition of SAMLG and SAWLG contrast metrics, fixes bug in checkerboard factory ([`2d135d1`](https://github.com/computational-psychology/stimupy/commit/2d135d10f3f4a48033bded5a9ff2fcc682cf39c9))

* corrects bug with sample_repeat not being an integer, checkerboard factory ([`239e114`](https://github.com/computational-psychology/stimupy/commit/239e1149295816a43cd6ca083577cdba57cf0f78))

* adds a version of SAWLG and SAMLG according to Moulden et al 1990, which differs to Robilotto 2002 ([`1711c53`](https://github.com/computational-psychology/stimupy/commit/1711c53724832d93be058fa51c2eab0438466cf6))

* fixed RMS contrast + added documentation ([`bebddec`](https://github.com/computational-psychology/stimupy/commit/bebddeca0d6ea5da0c55db01752580b6235e865a))

* removed chunk-mode from contrast metrics due to faulty logic ([`7b5fdb4`](https://github.com/computational-psychology/stimupy/commit/7b5fdb484498b4cd1ddf4d445753c968086512f4))

* added some tests in testing_contrast_metrics.py, not passing ([`90f37f3`](https://github.com/computational-psychology/stimupy/commit/90f37f34bdce2cd4159566e02ea0a9fe16393906))

* Update README.md ([`7bab0f8`](https://github.com/computational-psychology/stimupy/commit/7bab0f8f331b5d5cd718887048903b9bc4c25484))

* Update README.md ([`4165445`](https://github.com/computational-psychology/stimupy/commit/41654454477be5c7abf485130b8fe13b3d5d2472))

* Update README.md ([`b0eb8ce`](https://github.com/computational-psychology/stimupy/commit/b0eb8cef23b2756fdebfc18601a04485f7cc64fa))

* Update README.md ([`dc70915`](https://github.com/computational-psychology/stimupy/commit/dc70915b35112121f4fb79a9b403a9dafd490e37))

* Update README.md ([`07922cd`](https://github.com/computational-psychology/stimupy/commit/07922cd92fdeee7c7787518bf3b02c5d0e7e4fac))

* Update README.md ([`00372f6`](https://github.com/computational-psychology/stimupy/commit/00372f6c03bd13e50478022b6b65116701923d5b))

* fix ([`52da177`](https://github.com/computational-psychology/stimupy/commit/52da177ef96b0fd145d0916395011d2555e20bf7))

* fixed lightness and improved readmes ([`3edc235`](https://github.com/computational-psychology/stimupy/commit/3edc235c1f31993e465563f2d41b306724458b9e))

* readme update instructions ([`3d368a1`](https://github.com/computational-psychology/stimupy/commit/3d368a138207eb6c2a628ccceda47720e2bbca66))

* fixed contrast metrics ([`514219d`](https://github.com/computational-psychology/stimupy/commit/514219d5ca00582cb8b6fa04778e791083f0e1a5))

* minor fixes ([`97c4f15`](https://github.com/computational-psychology/stimupy/commit/97c4f158baf43ed91ae43621c35e9664edd8660c))

* fixed lightness stimuli ([`9468412`](https://github.com/computational-psychology/stimupy/commit/946841238fcb4e36c4e0b8eab7a739b6226d7b7f))

* main README edited ([`cfc4281`](https://github.com/computational-psychology/stimupy/commit/cfc42813f8b6337272a092c137f9bcfdf87b34cf))

* readme transparency edited ([`ba7f68c`](https://github.com/computational-psychology/stimupy/commit/ba7f68c3223ac8780dcfccd4b65f66f137184073))

* improving readme 3 ([`2259db0`](https://github.com/computational-psychology/stimupy/commit/2259db05365f4f3af8b9bc3847620e5b1f30db5f))

* improving readme 2 ([`beb22dc`](https://github.com/computational-psychology/stimupy/commit/beb22dc9bca3396ff6297c47373da17a4fc268cb))

* improving readmes ([`d951645`](https://github.com/computational-psychology/stimupy/commit/d951645c51413eba9ab4b8c0844d5bff53562cb6))

* fixed packaging-setup and added documentation ([`b9e7034`](https://github.com/computational-psychology/stimupy/commit/b9e70348448e19e425a3232d7a5db3c910a8e851))

* turned repo into an installable package ([`54ff1bb`](https://github.com/computational-psychology/stimupy/commit/54ff1bb12c9c46b0099e880e943fe135e73b14df))

* improved image factories and their documentation ([`aa5c247`](https://github.com/computational-psychology/stimupy/commit/aa5c24731494e58eae12a23c4f782ead546a2e80))

* change in comments ([`4fc18e0`](https://github.com/computational-psychology/stimupy/commit/4fc18e0b8eb44a79bb1227fda3cfc03f98566f5e))

* Update comments.md ([`c86d16c`](https://github.com/computational-psychology/stimupy/commit/c86d16c98d8eac3108aa69ecb9cdbd70785ab180))

* correction in documentation, removing checkerboard.png/pov, adding my comments ([`517c420`](https://github.com/computational-psychology/stimupy/commit/517c420183708f776b2ebe925c1ff2647d039eb6))

* added image generation factories for transparency experiments ([`203bec4`](https://github.com/computational-psychology/stimupy/commit/203bec420021f38a9af618fd37f57254a8db8df3))

* Merge branch `master` of github.com:TUBvision/stimuli ([`10181b9`](https://github.com/computational-psychology/stimupy/commit/10181b9a5fb76045d8f49063bcbeb5936236bbd6))

* Changes way of importing the module. ([`f997054`](https://github.com/computational-psychology/stimupy/commit/f997054f4e97a0964cd6585e8ab9f66c8abac4ef))

* Changes way of importing the module. ([`9058f8a`](https://github.com/computational-psychology/stimupy/commit/9058f8a8e671b2466bc6e03effec1043f2aeb2e4))

* added function to create smooth areas ([`7b604da`](https://github.com/computational-psychology/stimupy/commit/7b604da4813d2f9c0ca54ae0a6f77beb43596f80))

* fixing imports ([`00bdc30`](https://github.com/computational-psychology/stimupy/commit/00bdc30c54212672fbc3c319df3f3661b00f38cf))

* Merge branch `master` of https://github.com/TUBvision/stimuli ([`f218f05`](https://github.com/computational-psychology/stimupy/commit/f218f053aebd87346882680495760d5fdae17a2c))

* Added texture synthesis code for `polka dots` and `bricks` stimulus. ([`8379812`](https://github.com/computational-psychology/stimupy/commit/83798125c442b19f6d1afc93c96e99a634cd2b83))

* edited README files ([`57da8d2`](https://github.com/computational-psychology/stimupy/commit/57da8d29fc979c0c1977a0b729d0ec59199800ff))

* added documentation, minor changes to random_circles ([`4ec52bd`](https://github.com/computational-psychology/stimupy/commit/4ec52bd89146d8c7b1cd9b149a5989a7d39ff78d))

* added documentation ([`e8ed5bf`](https://github.com/computational-psychology/stimupy/commit/e8ed5bfbd65ede7d1b39f2f5fc16c19a5574efe2))

* Merge branch `master` of https://github.com/TUBvision/stimuli ([`f05aa0b`](https://github.com/computational-psychology/stimupy/commit/f05aa0bf6fbfa838cc2cde689bbcc187236d558a))

* added documentation ([`cf034c5`](https://github.com/computational-psychology/stimupy/commit/cf034c57d1f0ec49dfe176500a0102db52d12e02))

* texture init added ([`0f32290`](https://github.com/computational-psychology/stimupy/commit/0f32290b203b574c3827487bca79f73ec02b6662))

* mondrian and random circles moved to texture folder ([`b1a6b64`](https://github.com/computational-psychology/stimupy/commit/b1a6b64ba42a26b26f27746aed0bdb59bc9813a0))

* ignore ~ files ([`c0c6111`](https://github.com/computational-psychology/stimupy/commit/c0c61114985ec736e3e3b87f3e73f18599c12d84))

* lightness stimuli added from prev. repository. License updated. ([`ff342d8`](https://github.com/computational-psychology/stimupy/commit/ff342d8863c985d84bb8fa340ad1e090bbe14ffa))

* readme update ([`70aaf66`](https://github.com/computational-psychology/stimupy/commit/70aaf66d4fb44e3dae98b284043658bcb371be47))

* Initial commit ([`aef437f`](https://github.com/computational-psychology/stimupy/commit/aef437f7bc38238944971da62b08b935eb703187))
