def clean_currency(val):
    if isinstance(val, str):
        val = val.replace('$', '').replace(',', '').replace('(', '').replace(')', '').strip()
        if val == '-' or val == '0.00':
            return None
        return float(val)
    return val


class TestCleanCurrency:
    def test_dollar_sign_removal(self):
        """Test removal of dollar signs"""
        assert clean_currency("$100") == 100.0
        assert clean_currency("$1,000") == 1000.0
        assert clean_currency("$10.50") == 10.5

    def test_comma_removal(self):
        """Test removal of commas in large numbers"""
        assert clean_currency("1,000") == 1000.0
        assert clean_currency("1,000,000") == 1000000.0
        assert clean_currency("123,456.78") == 123456.78

    def test_parentheses_removal(self):
        """Test removal of parentheses (often used for negative values)"""
        assert clean_currency("(100)") == 100.0
        assert clean_currency("($100)") == 100.0
        assert clean_currency("(1,000)") == 1000.0

    def test_special_values(self):
        """Test special cases that should return None"""
        assert clean_currency("-") is None
        assert clean_currency("0.00") is None
        assert clean_currency(" - ") is None  # with whitespace
        assert clean_currency(" 0.00 ") is None  # with whitespace

    def test_whitespace_handling(self):
        """Test proper handling of whitespace"""
        assert clean_currency(" $100 ") == 100.0
        assert clean_currency("\t$1,000\n") == 1000.0
        assert clean_currency("   -   ") is None

    def test_combined_formatting(self):
        """Test strings with multiple formatting elements"""
        assert clean_currency("$(1,000.50)") == 1000.5
        assert clean_currency(" $ 1,234.56 ") == 1234.56
        assert clean_currency("($123,456.78)") == 123456.78

    def test_non_string_input(self):
        """Test that non-string inputs are returned unchanged"""
        assert clean_currency(100) == 100
        assert clean_currency(100.5) == 100.5
        assert clean_currency(None) is None
        assert clean_currency([1, 2, 3]) == [1, 2, 3]

    def test_float_conversion(self):
        """Test proper conversion to float"""
        result = clean_currency("$100")
        assert isinstance(result, float)
        assert result == 100.0

    def test_negative_numbers(self):
        """Test handling of negative numbers (not with parentheses)"""
        assert clean_currency("-$100") == -100.0
        assert clean_currency("-$1,000.50") == -1000.5
        assert clean_currency("$-123.45") == -123.45

    def test_zero_values(self):
        """Test various zero representations"""
        assert clean_currency("0.00") is None
        assert clean_currency("$0.00") is None
        assert clean_currency("0") == 0.0
        assert clean_currency("$0") == 0.0
        assert clean_currency("$0.01") == 0.01