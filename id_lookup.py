from baseball_id import Lookup
import pandas as pd

# pd.set_option('display.max_columns', None)


print(
    Lookup.from_names(
        [
            "Corbin Carroll",
            "Ketel Marte",
            "Gabriel Moreno",
            "Christian Walker",
            "Tommy Pham",
            "Lourdes Gurriel Jr.",
            "Alek Thomas",
            "Evan Longoria",
            "Geraldo Perdomo",
        ]
    )
)
