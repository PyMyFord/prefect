# Notes

An `error` in a JSON response seems to indicate an authentication error, whereas a `status` code seems to indicate something more nuanced.

Planning to add a high-level API where a Vehicle object can auto-select itself from the user's account (rather than having to `.select_vehicle` every time you want to talk to a car) and handle its own endpoints by operating on a FordAPI low-level API.
