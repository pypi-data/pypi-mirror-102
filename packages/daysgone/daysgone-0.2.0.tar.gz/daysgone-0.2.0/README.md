# `daysgone`

This is a cli that outputs dates.

**Usage**:

```console
$ daysgone [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `adddays`: Add number of days and date to get the number...
* `daterange`: Enter a start date and end date to get a list...
* `daysago`: Enther the number of days you want to go back...
* `daysfromnow`: Enter the number of days to get the date.
* `diff`: Calculates difference in days between two...
* `isweekday`: Find out if the date is a weekend or date.
* `isweekend`: Check if given date is a weekend.

## `daysgone adddays`

Add number of days and date to get the number of days.

If no date is given, then todays date will be used.

**Usage**:

```console
$ daysgone adddays [OPTIONS] DAYS
```

**Arguments**:

* `DAYS`: Number of days from date given.  [required]

**Options**:

* `-d, --date TEXT`: Enter date in this format: MM-DD-YYYY
* `--help`: Show this message and exit.

## `daysgone daterange`

Enter a start date and end date to get a list of dates between.

**Usage**:

```console
$ daysgone daterange [OPTIONS] START END
```

**Arguments**:

* `START`: Enter the start date  [required]
* `END`: Enter the end date  [required]

**Options**:

* `--help`: Show this message and exit.

## `daysgone daysago`

Enther the number of days you want to go back to.

**Usage**:

```console
$ daysgone daysago [OPTIONS] DAYS
```

**Arguments**:

* `DAYS`: Number of days you want to go back to.  [required]

**Options**:

* `--help`: Show this message and exit.

## `daysgone daysfromnow`

Enter the number of days to get the date.

**Usage**:

```console
$ daysgone daysfromnow [OPTIONS] DAYS
```

**Arguments**:

* `DAYS`: Get day from number of days given.  [required]

**Options**:

* `--help`: Show this message and exit.

## `daysgone diff`

Calculates difference in days between two dates.

**Usage**:

```console
$ daysgone diff [OPTIONS] START END
```

**Arguments**:

* `START`: Start date. Format: MM-DD-YYYY  [required]
* `END`: End date. Format: MM-DD-YYYY  [required]

**Options**:

* `--help`: Show this message and exit.

## `daysgone isweekday`

Find out if the date is a weekend or date.

**Usage**:

```console
$ daysgone isweekday [OPTIONS] DATE
```

**Arguments**:

* `DATE`: Enter date in this format: MM-DD-YYYY  [required]

**Options**:

* `--help`: Show this message and exit.

## `daysgone isweekend`

Check if given date is a weekend.

**Usage**:

```console
$ daysgone isweekend [OPTIONS] DATE
```

**Arguments**:

* `DATE`: Enter date in this format: MM-DD-YYYY  [required]

**Options**:

* `--help`: Show this message and exit.
