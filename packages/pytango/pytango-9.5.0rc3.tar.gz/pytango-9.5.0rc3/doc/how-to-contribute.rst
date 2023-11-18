.. currentmodule:: tango

.. highlight:: python
   :linenothreshold: 3

.. _how-to-contribute:

=================
How to Contribute
=================

Everyone is welcome to contribute to PyTango project.
If you don't feel comfortable with writing core PyTango we are looking for contributors to documentation or/and tests.

Workflow
--------

A Git feature branch workflow is used. More details can be seen in this tutorial_.
Good practices:

* For commit messages the first line should be short (50 chars or less) and contain a summary
  of all changes. Provide more detail in additional paragraphs unless the change is trivial.
* Merge requests (MRs) should be ALWAYS made to the ``develop`` branch.

reStructuredText and Sphinx
---------------------------

Documentation is written in reStructuredText_ and built with Sphinx_ - it's easy to contribute.
It also uses autodoc_ importing docstrings from tango package.
Theme is not important, a theme prepared for Tango Community can be also used.

To test the docs locally (work in a virtualenv):
      - ``$ cd /path/to/pytango``
      - ``$ python -m pip install -r doc/requirements.txt``
      - ``$ python -m sphinx doc build/sphinx``

To test the docs locally in a Sphinx Docker container:
      - ``(host) $ cd /path/to/pytango``
      - ``(host) $ docker run --rm -ti -v $PWD:/docs sphinxdoc/sphinx bash``
      - ``(container) $ python -m pip install gevent numpy packaging pillow psutil sphinx_rtd_theme``
      - ``(container) $ python -m sphinx doc build/sphinx``

After building, open the ``build/doc/index.html`` page in your browser.

Source code standard
--------------------

All code should be PEP8_ compatible. We have set up checking code quality with
pre-commit_ which runs ruff_, a Python linter written in Rust. ``pre-commit`` is
run as first job in every gitlab-ci pipeline and will fail if errors are detected.

It is recommended to install pre-commit_ locally to check code quality on every commit,
before to push to GitLab. This is a one time operation:

* Install pre-commit_. pipx_ is a good way if you use it.
  Otherwise, see the `official documentation <https://pre-commit.com/#install>`_.
* Run ``pre-commit install`` at the root of your ``pytango`` repository.

That's it. ``pre-commit`` will now run automatically on every commit.
If errors are reported, the commit will be aborted.
You should fix them and try to commit again.

Note that you can also configure your editor to run `ruff`.
See `ruff README <https://github.com/charliermarsh/ruff#editor-integrations>`_.


.. _tutorial: https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow
.. _autodoc: https://pypi.python.org/pypi/autodoc
.. _PEP8: https://peps.python.org/pep-0008/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://www.sphinx-doc.org/en/stable
.. _pre-commit: https://pre-commit.com
.. _ruff: https://github.com/charliermarsh/ruff
.. _pipx: https://pypa.github.io/pipx/


.. _conda-for-development:

Using Conda for development
---------------------------

For local development, it is recommended to work in a :ref:`Conda environment <build-from-source>`.

To run the tests locally (after activating your Conda environment):
      - ``$ pytest``

To run only some tests, use a filter argument, ``-k``:
      - ``$ pytest -k test_ping``


Using Docker for development
----------------------------

Docker containers are useful for developing, testing and debugging PyTango.  See the
folder ``.devcontainer`` in the root of the source repo.  It includes instructions for
building the Docker images and using them for development.

For direct usage, rather than PyTango developement, Docker images with PyTango already
installed are available from the
`Square Kilometre Array Organisation's repository <https://artefact.skao.int/#browse/search/docker=format=docker%20AND%20attributes.docker.imageName=ska-tango-images-tango-pytango>`_.

For example:
 - ``docker run --rm -ti artefact.skao.int/ska-tango-images-tango-pytango:9.4.3``


Releasing a new version
-----------------------

Starting from 9.4.2 pytango tries to follow cpptango releases with the delay up to ~1 month.
The basic steps to make a new release are as follows:

Pick a version number
  * A 3-part version numbering scheme is used:  <major>.<minor>.<patch>
  * Note that PyTango **does not** follow `Semantic Versioning <https://semver.org>`_.
    API changes can occur at minor releases (but avoid them if at all possible).
  * The major and minor version fields (e.g., 9.4) track the TANGO C++ core version.
  * Small changes are done as patch releases.  For these the version
    number should correspond the current development number since each
    release process finishes with a version bump.
  * Patch release example:
      - ``9.4.4.devN`` or ``9.4.4rcN`` (current development branch)
      - changes to ``9.4.4`` (the actual release)
      - changes to ``9.4.5.dev0`` (bump the patch version at the end of the release process)
  * Minor release example:
      - ``9.4.4.devN`` or ``9.4.4rcN`` (current development branch)
      - changes to ``9.5.0`` (the actual release)
      - changes to ``9.5.1.dev0`` (bump the patch version at the end of the release process)

Check which versions of Python should this release support
 * Follow the :ref:`version policy <pytango-version-policy>` and modify correspondingly `requires-python`, `classifiers`,
   and minimum runtime `dependencies` for NumPy in `pyproject.toml`.

Create an issue in GitLab
  * This is to inform the community that a release is planned.
  * Use a checklist similar to the one below:

    | Task list:
    | - [ ] Read steps in the how-to-contribute docs for making a release
    | - [ ] Merge request to update changelog and bump version
    | - [ ] Merge MR (this is the last MR for the release)
    | - [ ] Make sure CI is OK on develop branch
    | - [ ] Make sure the documentation is updated for develop (readthedocs)
    | - [ ] Create an annotated tag from develop branch
    | - [ ] Push stable to head of develop
    | - [ ] Make sure the documentation is updated for release (readthedocs)
    | - [ ] Upload the new version to PyPI
    | - [ ] Bump the version with "-dev" in the develop branch
    | - [ ] Create and fill in the release description on GitLab
    | - [ ] Build conda packages
    | - [ ] Advertise the release on the mailing list
    | - [ ] Close this issue

  * A check list in this form on GitLab can be ticked off as the work progresses.

Make a branch from ``develop`` to prepare the release
  * Example branch name: ``prepare-v9.4.4``.
  * Edit the changelog (in ``docs/revision.rst``).  Include *all* merge requests
    since the version was bumped after the previous release.  Reverted merge
    requests can be omitted.  A command like this could be used to see all the MR numbers, just change the
    initial version:
    ``git log --ancestry-path v9.4.3..develop | grep "merge request" | sort``
  * Find the versions of the dependencies included in our binary PyPI packages, and update this in ``docs/news.rst``.
      - For Linux, see `PyTango CI wheel-linux config <https://gitlab.com/tango-controls/pytango/-/blob/c0812e6b50aca9225939ad6d95bf9546736fac4d/.gitlab-ci.yml#L35>`_,
        and `pytango-builder tags <https://gitlab.com/tango-controls/docker/pytango-builder/-/tags>`_,
      - For Windows:  See `cppTango CI config <https://gitlab.com/tango-controls/cppTango/-/blob/9.5.0/.windows-gitlab-ci.yml?ref_type=tags#L17-21>`_,
        `zmq-windows-ci CI config <https://github.com/tango-controls/zmq-windows-ci/blob/master/appveyor.yml>`_,
        and `PyTango CI wheel-win config <https://gitlab.com/tango-controls/pytango/-/blob/c0812e6b50aca9225939ad6d95bf9546736fac4d/.gitlab-ci.yml#L72>`_.
      - For macOS:  see PyTango CI output, and `cpptango conda-forge feedstock <https://github.com/conda-forge/cpptango-feedstock/>`_
        CI output (for tango-idl).
  * Bump the versions (``tango/release.py``, ``pyproject.toml`` and ``CMakeLists.txt``).
    E.g. ``version_info = (9, 4, 4)``, ``version = "9.4.4"``, and ``VERSION 9.4.4`` for a final release.  Or, for
    a release candidate: ``version_info = (9, 4, 4, "rc", 1)``, ``version = "9.4.4.rc1"``, and ``VERSION 9.4.4``.
  * Create a merge request to get these changes reviewed and merged before proceeding.

Make sure CI is OK on ``develop`` branch
  * On Gitlab CI all tests, on all versions of Python, must be passing.
    If not, bad luck - you'll have to fix it first, and go back a few steps...

Make sure the documentation is updated
  * Log in to https://readthedocs.org.
  * Get account permissions for https://readthedocs.org/projects/pytango from another
    contributor, if necessary.
  * Readthedocs *should* automatically build the docs for each:
      - push to develop (latest docs)
      - new tags (e.g v9.4.4)
  * *But*, the webhooks are somehow broken, so it probably won't work automatically!
      - Trigger the builds manually here:  https://readthedocs.org/projects/pytango/builds/
      - Set the new version to "active" here:
        https://readthedocs.org/dashboard/pytango/versions/

Create an annotated tag for the release
  * GitLab's can be used to create the tag, but a message must be included.
    We don't want lightweight tags.
  * Alternatively, create tag from the command line (e.g., for version 9.4.4):
      - ``$ git checkout develop``
      - ``$ git pull``
      - ``$ git tag -a -m "tag v9.4.4" v9.4.4``
      - ``$ git push -v origin refs/tags/v9.4.4``

Push ``stable`` to head of ``develop``
  * **Skip this step for release candidates!**
  * Merge ``stable`` into the latest ``develop``.  It is recommended to do a
    fast-forward merge in order to avoid a confusing merge commit. This can be
    done by simply pushing ``develop`` to ``stable`` using this command:

      ``$ git push origin develop:stable``

    This way the release tag corresponds to the actual release commit both on the
    ``stable`` and ``develop`` branches.
  * In general, the ``stable`` branch should point to the latest release.

Upload the new version to PyPI
  * The source tarball and binary wheels are automatically uploaded to PyPI by Gitlab CI on tag.

Bump the version with "-dev" in the develop branch
  * Make a branch like ``bump-dev-version`` from head of ``develop``.
  * In ``tango/release.py``, change ``version_info``, e.g. from ``(9, 4, 4)`` to
    ``(9, 4, 5, "dev", 0)``.
  * In ``pyproject.toml``, change ``version``, e.g. from ``"9.4.4"`` to
    ``"9.4.5.dev0"``.
  * In ``CMakeLists.txt``, change ``VERSION``, e.g. from ``9.4.4`` to
    ``9.4.5.0``.
  * Create MR, merge to ``develop``.

Create and fill in the release description on GitLab
  * Go to the Tags page: https://gitlab.com/tango-controls/pytango/-/tags
  * Find the tag created above and click "Edit release notes".
  * Content must be the same as the details in the changelog.  List all the
    merge requests since the previous version.

Build conda packages
  * Conda-forge is used to build these. See https://github.com/conda-forge/pytango-feedstock
  * A new pull request should be created automatically by the Conda forge bot after our tag.
  * Get it merged by one of the maintainers.

Advertise the release on the mailing list
  * Post on the Python development list.
  * Example of a previous post:  http://www.tango-controls.org/community/forum/c/development/python/pytango-921-release/

Close off release issue
  * All the items on the check list should be ticked off by now.
  * Close the issue.
