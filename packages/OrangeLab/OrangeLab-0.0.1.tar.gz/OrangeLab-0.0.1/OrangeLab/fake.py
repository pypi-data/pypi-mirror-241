import pandas as pd
from faker import Faker

def supported_types():
    """
    Returns a list of supported types for generating fake data using the Faker module.

    Returns:
        list: A list of strings representing the supported types.

    Example:
        >>> supported_types()
        ['aba', 'add_provider', 'address', 'administrative_unit', 'am_pm', 'android_platform_token', 'ascii_company_email', 'ascii_email', 'ascii_free_email', 'ascii_safe_email', 'bank_country', ...]
    """
    Types = [ "aba", "add_provider", "address", "administrative_unit", "am_pm", "android_platform_token", "ascii_company_email", "ascii_email", "ascii_free_email", "ascii_safe_email", "bank_country", "basic_phone_number", "bban", "binary", "boolean", "bothify", "bs", "building_number", "cache_pattern", "catch_phrase", "century", "chrome", "city", "city_prefix", "city_suffix", "color", "color_hsl", "color_hsv", "color_name", "color_rgb", "color_rgb_float", "company", "company_email", "company_suffix", "coordinate", "country", "country_calling_code", "country_code", "credit_card_expire", "credit_card_full", "credit_card_number", "credit_card_provider", "credit_card_security_code", "cryptocurrency", "cryptocurrency_code", "cryptocurrency_name", "csv", "currency", "currency_code", "currency_name", "currency_symbol", "current_country", "current_country_code", "date", "date_between", "date_between_dates", "date_object", "date_of_birth", "date_this_century", "date_this_decade", "date_this_month", "date_this_year", "date_time", "date_time_ad", "date_time_between", "date_time_between_dates", "date_time_this_century", "date_time_this_decade", "date_time_this_month", "date_time_this_year", "day_of_month", "day_of_week", "del_arguments", "dga", "domain_name", "domain_word", "dsv", "ean", "ean13", "ean8", "ein", "email", "emoji", "enum", "factories", "file_extension", "file_name", "file_path", "firefox", "first_name", "first_name_female", "first_name_male", "first_name_nonbinary", "fixed_width", "format", "free_email", "free_email_domain", "future_date", "future_datetime", "generator_attrs", "get_arguments", "get_formatter", "get_providers", "hex_color", "hexify", "hostname", "http_method", "iana_id", "iban", "image", "image_url", "internet_explorer", "invalid_ssn", "ios_platform_token", "ipv4", "ipv4_network_class", "ipv4_private", "ipv4_public", "ipv6", "isbn10", "isbn13", "iso8601", "items", "itin", "job", "json", "json_bytes", "language_code", "language_name", "last_name", "last_name_female", "last_name_male", "last_name_nonbinary", "latitude", "latlng", "lexify", "license_plate", "linux_platform_token", "linux_processor", "local_latlng", "locale", "locales", "localized_ean", "localized_ean13", "localized_ean8", "location_on_land", "longitude", "mac_address", "mac_platform_token", "mac_processor", "md5", "military_apo", "military_dpo", "military_ship", "military_state", "mime_type", "month", "month_name", "msisdn", "name", "name_female", "name_male", "name_nonbinary", "nic_handle", "nic_handles", "null_boolean", "numerify", "opera", "optional", "paragraph", "paragraphs", "parse", "passport_dates", "passport_dob", "passport_full", "passport_gender", "passport_number", "passport_owner", "password", "past_date", "past_datetime", "phone_number", "port_number", "postalcode", "postalcode_in_state", "postalcode_plus4", "postcode", "postcode_in_state", "prefix", "prefix_female", "prefix_male", "prefix_nonbinary", "pricetag", "profile", "provider", "providers", "psv", "pybool", "pydecimal", "pydict", "pyfloat", "pyint", "pyiterable", "pylist", "pyobject", "pyset", "pystr", "pystr_format", "pystruct", "pytimezone", "pytuple", "random", "random_choices", "random_digit", "random_digit_above_two", "random_digit_not_null", "random_digit_not_null_or_empty", "random_digit_or_empty", "random_element", "random_elements", "random_int", "random_letter", "random_letters", "random_lowercase_letter", "random_number", "random_sample", "random_uppercase_letter", "randomize_nb_elements", "rgb_color", "rgb_css_color", "ripe_id", "safari", "safe_color_name", "safe_domain_name", "safe_email", "safe_hex_color", "sbn9", "secondary_address", "seed", "seed_instance", "seed_locale", "sentence", "sentences", "set_arguments", "set_formatter", "sha1", "sha256", "simple_profile", "slug", "ssn", "state", "state_abbr", "street_address", "street_name", "street_suffix", "suffix", "suffix_female", "suffix_male", "suffix_nonbinary", "swift", "swift11", "swift8", "tar", "text", "texts", "time", "time_delta", "time_object", "time_series", "timezone", "tld", "tsv", "unique", "unix_device", "unix_partition", "unix_time", "upc_a", "upc_e", "uri", "uri_extension", "uri_page", "uri_path", "url", "user_agent", "user_name", "uuid4", "vin", "weights", "windows_platform_token", "word", "words", "xml", "year", "zip", "zipcode", "zipcode_in_state", "zipcode_plus4"]
    return Types

def generate_fake_dataset(num_rows, path="fake_dataset.csv", none_values=True, table_head=None):
    # Create a Faker instance
    fake = Faker()

    # Create an empty DataFrame with the specified column names
    columns = list(table_head.keys())
    df = pd.DataFrame(columns=columns)

    # Generate fake data for each column
    for col, config in table_head.items():
        data_type = config.get("type")
        dtype = config.get("dtype")
        col_data = []

        for _ in range(num_rows):
            if data_type:
                col_data.append(getattr(fake, data_type)())
            elif dtype == "int":
                if "range" in config:
                    start, end = map(int, config["range"].split("-"))
                    col_data.append(fake.random_int(min=start, max=end))
                elif "len" in config:
                    col_data.append(fake.random_int(min=10**(config["len"]-1), max=(10**config["len"])-1))
            else:
                col_data.append(None if none_values else "N/A")

        df[col] = col_data

    # Export DataFrame to the specified file type
    if "csv" in path.split("."):
        df.to_csv(path, index=False)
    elif "json" in path.split("."):
        df.to_json("fake_dataset.json", orient="records", lines=True)
    elif "xlsx" in path.split("."):
        df.to_excel("fake_dataset.xlsx", index=False)
    elif "tsv" in path.split("."):
        df.to_csv("fake_dataset.tsv", index=False, sep="\t")

# Example usage
num_rows = 500
filetype = "sample.csv"
none_values = True
# table_head = {
#     "name": {"type": "name"},
#     "email": {"type": "email"},
#     "phn_no": {"dtype": "int", "len": 10},
#     "age": {"dtype": "int", "range": "1-100"},
#     "drinking_water":{"dtype":"int","range":"1-10"}
# }

table_head = {
    "name":{"type":"name"},
    "email":{"type":"email"},
    "gender":{"type":"passport_gender"},
    "age":{"dtype":"int","range":"10-100"},
    "score":{"dtype":"int","range":"10-100"},
    "time_s":{"dtype":"int","range":"10-100"},
}

generate_fake_dataset(num_rows, filetype, none_values, table_head)

