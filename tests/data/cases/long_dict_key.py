tests = [
    (
        BusinessHour(),
        {
            Timestamp("2014-07-04 15:00") + Nano(5): (
                this_is_a_very_long_function("2014-07-04 16:00")
            ),
            Timestamp("2014-07-04 16:00") + Nano(5): (
                this_is_a_very_long_function("2014-07-04 16:00"),
            ),
            Timestamp("2014-07-04 16:00") - Nano(5): (
                this_is_a_very_long_function("2014-07-04 16:00")
            ),
        },
    ),
]

# output

tests = [
    (
        BusinessHour(),
        {
            Timestamp("2014-07-04 15:00") + Nano(5): (
                this_is_a_very_long_function("2014-07-04 16:00")
            ),
            Timestamp("2014-07-04 16:00") + Nano(5): (
                this_is_a_very_long_function("2014-07-04 16:00"),
            ),
            Timestamp("2014-07-04 16:00") - Nano(5): (
                this_is_a_very_long_function("2014-07-04 16:00")
            ),
        },
    ),
]
