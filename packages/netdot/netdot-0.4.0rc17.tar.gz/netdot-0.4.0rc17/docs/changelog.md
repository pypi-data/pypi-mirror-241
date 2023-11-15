# Changelog
<a id="changelog"></a>
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

> Notice: Major version zero (0.y.z) is for initial development. Anything MAY change at any time.
> This public API should **not** be considered stable.

> ⚠ Disclaimer: From 0.2.0 onward, this API wrapper does not ensure support for the [de facto Open Source version of NetDot (GitHub)](https://github.com/cvicente/Netdot).

## [Unreleased]
<a id="unreleased"></a>

* Generate a prettier document for ["Feature Flags" Environment Variables](./generated-env-var-docs.md).
    * Today, we [ab]use [configargparse](https://pypi.org/project/ConfigArgParse/) to generate that documentation.
* Ensure compatibility with the [de facto Open Source version of NetDot (GitHub)](https://github.com/cvicente/Netdot).
* Wire up the `UnitOfWork.dry_run` (aka `Repository.show_changes`) to use DISPLAY_ATTRIBUTES when defaults.DISPLAY_FULL_OBJECTS=False.
* More mechanisms for saving UnitOfWork (aka proposed_changes) to a file:
    * `save_as_excel` would be great to save all proposed changes as a workbook.
    * `save_as_CSVs` would be great to save all proposed changes as a set of CSV files.
* Documentation for the fact that: "`urllib3.exceptions.ProtocolError` can occur during any API request."
* There are still 2 Python Dataclasses that just need to be implemented:
    - [ ] ARPCache
    - [ ] ARPCacheEntry 
* Retrieve/update various data types that contain **binary blobs** via REST API:
    - [ ] DataCaches
    - [ ] ClosetPictures
    - [ ] SitePictures
    - [ ] FloorPictures
* Continuous Integration: Generating 'badges' for 'code coverage' and 'tests passing' would be nice to have.


## [0.4.0]

### Added

* Python 3.6 compatibility
* ["Feature Flags" Environment Variables](./generated-env-var-docs.md)
> ℹ Use `netdot.defaults.help()` to see full info.
* [API documentation](./generated-api-docs.md) for this Python Netdot API Wrapper.
* Support for 'Dry Runs' when making updates (i.e. create, update, delete).
    > See ["Example 8: Plan and Create a New Netdot Site" in the User Guide](./user-guide.md#example-8-plan-and-create-a-new-netdot-site)
    1. Automatically set up a UnitOfWork when calling `netdot.connect`
    > ℹ Bypass 'dry runs' feature via `netdot.connect(propose_changes=False)` or after the fact using `disable_propose_changes()`.
    >
    > ℹ To selectively enable the 'dry runs' features on a Repository, use `enable_propose_changes(print_changes=..., auto_update=...)`
    2. Make changes just like normal.
    3. Show any proposed changes using `show_changes` or `show_changes_as_tables`.
    > ℹ You can select which columns render via `show_changes_as_tables(select_cols=[...])` 
    >
    > ℹ You can render the full nested objects via `show_changes_as_tables(display_full_objects=True)` 
    >
    >```python
    >>>> show_changes_as_tables(select_cols=['name', 'label', 'address'])`
    >
    >## Room Changes
    >
    >action    id    name
    >--------  ----  -----------
    >CREATE    None  Test Room 1
    >
    >## Audit Changes
    >
    >action    id    label
    >--------  ----  -----
    >CREATE    None  None
    >```
    >
    > ℹ You can control the CLI output (for smaller screens) in these using  `show_changes(terse=True)` or `show_changes_as_tables(terse=True)``. 
    >> ℹ To make your 'terse' setting persistent, see `NETDOT_CLI_TERSE` and related environment variables in the ["Feature Flags" Environment Variables](./generated-env-var-docs.md)
    4. Save those changes using `save_changes`
    > ℹ If any DELETEs are planned: `save_changes` will asks the user for confirmation (unless you call `save_changes(confirm=False)`)
* After calling `save_changes`, use `show_all_changes` to see a report of **all** actions.
    * includes completed tasks,
    * includes planned tasks, and
    * *if there was a failure*, includes the latest failed task.
* The `UnitOfWork` supports [`save_as_pickle` to save any proposed changes to a file](./user-guide.md#proposed-changes-pickle-file-save_as_pickle-and-load).
> ℹ NOTE: Be sure to record which version of this `netdot` python package you are using (to ensure future parsability).
>
> It is wise to include `netdot-cli-{netdot.__version__}` in your f-string filename.
```python
# Save any proposed changes to a file
filename = f'netdot-cli-{netdot.__version__}-UnitOfWork.pickle'
nd_repo.proposed_changes.save_as(filename)
```
```python
# Either Load it directly (without needing a Netdot connection)
proposed_changes = netdot.load(filename)

# Or Load it back into your Repository (to resume making changes)
nd_repo.proposed_changes.load(filename)
``` 
* Implemented Python Dataclasses for *most* all of the Netdot Database schema.
    * All except two ArpCache data types and the four 'binary blob' containing data types, all listed in [Unreleased](#unreleased).
* Basic '**C**R**UD**' methods on each NetdotAPIDataclass:
    * `create_or_update`: Create or update this object in Netdot.
    * `create`: *Thin wrapper around `create_or_update`.*
    * `update`: *Thin wrapper around `create_or_update`.*
    * `delete`: Delete this object in Netdot.
        * Asks for user confirmation (unless you call `delete(confirm=False)`)
* Generate methods on each NetdotAPIDataclass:
    * `add_*` methods for 1-to-many relationships.
        * Examples: `site.add_device` or `site.add_sitelink_as_farend`
    * `add_*` methods for many-to-many relationships.
        * Examples: `site.add_subnet` (and the more obscure `site.add_sitesubnet`)
    * †`load_*` methods for 1-to-many relationships.
        * Examples: `site.load_devices`
    * †`load_*` methods for many-to-many relationships.
        * Examples: `site.load_subnets`
    > †: `load_*` methods will catch any HTTP 404 errors and instead return Empty List or None.
    > (Use `ignore_404=False` to raise HTTP 404 errors instead)
* [UNTESTED] Log a warning whenever 'Carp::croak' is returned in HTTP response.


### Changed

* `web_url` property tested for ***all** Netdot objects.*
    * web_url is: "A URL to view this object in Netdot's web interface."
    * Now using the simple "/generic/view.html" endpoint (instead of trying to use a more a 'more applicable webpage' for each data type).
* Fix pluralization for various methods in [public API](./generated-api-docs.md).
* Simplified NetdotAPIDataclass property setters (by overwriting `__setattr__` directly for NetdotAPIDataclass).
    * ❌ Old way:
    ```
    netdot.Floor(...).with_site(site)
    ```
    * ✅ New way, via `__init__`:
    ```
    floor = netdot.Floor(..., site=site, ...)
    ```
  * ✅ New way, via assignment operator (`=`):
    ```
    floor = netdot.Floor(...)
    floor.site = site
    ```
* DownloadTracer is now optional and more resilient:
    * DownloadTracer is now an opt-in feature, configurable via ["Feature Flags" Environment Variables](./generated-env-var-docs.md), and
    * DownloadTracer now does all its logging via asyncio (to ensure that logging doesn't interrupt your downloads)

### Removed

* No longer generate the `with_*` and `set_*` methods for NetdotAPIDataclass.
* Do not log a warning when 'info' or 'ttl' are absent from HTTP Response (they are VERY optional)
    * Search for `inconsistent_and_ignorable_fields` to learn more
* Removed old `netdot.Connect` class entirely



## [0.3.2]

* Enable looking up a DNS Resource Record (RR) by address, using `repo.get_rr_by_address()`

## [0.3.1]

* Speed up `find_edge_port`.
  * HTTP requests are parallelized via multithreading where possible.

## [0.3.0]

> ⚠ Breaking Backwards Compatibility: Several `netdot.Repository` methods are renamed, as discussed below.

* Add `Repository.find_edge_port(mac_address)` method.
  * This requires a lot of HTTP requests since we do not have the ability to run arbitrary database queries (SQL JOIN behavior is unavailable via RESTful interface).
* Wired up the following netdot.dataclasses:
  * `ForwardingTable`
  * `ForwardingTableEntry`
  * `PhysAddr`
* Renamed several generated methods to end in "ies" instead of "ys" when pluralized.
* Dropping Python 3.6 and 3.7 compatibility (required to use [hatch](https://github.com/pypa/hatch))

## [0.2.6]

* Fix typo in `MACAddress:format` method argument: "delimiter" becomes "delimiter"
  * Additionally, force keyword arguments for the `format`using Python 3 feature.

## [0.2.5]

* In `netdot.Client` the base `delete(..., id)` method can now accept an `int`.
  * Before, it only accepted `str`.

## [0.2.4]

* Gracefully handle response from HTTP Delete requests when possible.
  * Delete seems to return 'empty' (a couple of newlines actually) on success.

## [0.2.3]

* Enable a `replace` function for all `netdot.dataclasses`
  * This makes it easier to do 'update' like operations using this library.

## [0.2.2]

* Fix for REGRESSION: The `post` method of `netdot.Client` does not work.
  * Debugged using a simple automated test (captured by a PyVCR Cassette for reproducibility)

## [0.2.1]

> 🐛 REGRESSION: The `post` method of `netdot.Client` does not work!

* Fix for REGRESSION: The `netdot.Client.Connection` class is missing!
  * Re-added `Connection` directly to client.py for now.
  * Aliased `netdot.client` module to also be available as it was formerly named, `netdot.Client` (pep8 suggests lowercase module names instead of CamelCase).
    * Using `__all__` in "netdot/\_\_init\_\_.py"

## [0.2.0]

> 🐛 REGRESSION: The `netdot.Client.Connection` class is MISSING!

> ⚠ We have not ensured support for the [de facto Open Source version of NetDot (GitHub)](https://github.com/cvicente/Netdot).

* Introducing a new layer of abstraction -- a Repository and many Python dataclasses.
  * See more info in the [User Guide](user-guide.md)
* Provide technical documentation in "docs/" directory (following NTS's standards).

## [0.1.0]

* Provide Python Netdot Client, as originally authored by Francisco Gray.
