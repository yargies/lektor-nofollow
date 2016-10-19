# lektor-nofollow
This plugin allows easy creation of nofollow links in markdown. Simply precede the link url with a ! (exclamation point).

Example:

	[google](!http://google.com)

Will generate:

	<a href="http://google.com" rel="nofollow">google</a>

## Installation
Add lektor-nofollow to your project from command line:

    lektor plugins add lektor-nofollow

See the Lektor documentation for more instructions on installing plugins.