# Contributing

Provide exact model/firmware, package revision, date, test and limitation. Prefer primary sources. Mark anecdotes as such; do not infer compatibility across generations.

Use synthetic temporary fixtures. No real books, private settings, credentials, firmware, dictionaries or device-generated patches in Git.

~~~text
python -m unittest discover -s tests -v
~~~

No third-party packages needed. An OS symlink test may skip where creation privileges are unavailable; the refusal branch is also tested without that privilege.

Keep offline default. Optional additions need benefit, dependencies, power behavior, stop/uninstall/recovery and failure tests. No universal compatibility, human-review badges or unmeasured performance claims. Attribute upstream work; do not relicense it.
