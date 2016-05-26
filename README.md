Click to Shell
==============

Redirects phone links like `callto:`, `tel:`, or `sms:` to a user-provided shell script.

How to install on a Mac
=======================

Download the latest release of this project and move the `clicktoshell.app` file in `/Applications` (or somewhere else).

You should also install [RCDefaultApp](http://www.rubicode.com/Software/RCDefaultApp/) to make it easy to register the right protocol handlers.

In RCDefaultApp, go to the "URL" tab, select `callto` for instance, then select `clicktoshell.app` as a default app.

Then, create a file `clicktoshell-callto.sh` in your user directory (for instance, `/Users/Bob/clicktoshell-callto.sh`).

This shell script will get executed each time the user clicks a `callto:` link, with the phone (formatted in international format) as first argument.

An example of script using the [Keyyo VoIP API](https://api.keyyo.com/developers/):

```
curl https://ssl.keyyo.com/makecall.html?ACCOUNT=+33111111111&CALLEE=$1&CALLEE_NAME=Keyyo
```