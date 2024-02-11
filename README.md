CSViewer - tratatatatata

There is a standart RFC 4180 designed to standardize and simplify the exchange of data in CSV format.
RFC 4180 requires follows:
- MS-DOS-style lines that end with (CR/LF) characters (optional for the last line).
- An optional header record (there is no sure way to detect whether it is present, so care is required when importing).
- Each record should contain the same number of comma-separated fields.
- Any field may be quoted (with double quotes).
- Fields containing a line-break, double-quote or commas should be quoted. (If they are not, the file will likely be impossible to process correctly.)
- If double-quotes are used to enclose fields, then a double-quote in a field must be represented by two double-quote characters.

This code expects not even comma as a delimiter, but every symbol from list [ ,|;] too. Because of this CSViewer requires one more condition:
- Fields containing any symbol above should be quoted too.