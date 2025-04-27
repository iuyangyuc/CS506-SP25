import pandas as pd


def correct_hours_worked(val):
    if pd.isna(val):
        return None
    try:
        val_int = int(val)
        if 0 <= val < 24:
            return float(val)
        elif 100 <= val_int <= 2400:
            hours = val_int // 100
            minutes = val_int % 100
            return hours + minutes / 60
        else:
            return None
    except:
        return None


def test_correct_hours_worked_with_pytest():

    assert correct_hours_worked(8.5) == 8.5
    assert correct_hours_worked(0) == 0.0
    assert correct_hours_worked(23.99) == 23.99


    assert correct_hours_worked(1230) == 12.5
    assert correct_hours_worked(2345) == 23.75

    assert correct_hours_worked(-5) is None
    assert correct_hours_worked(25) is None
    assert correct_hours_worked(3000) is None

    assert correct_hours_worked(pd.NA) is None
    assert correct_hours_worked(float('nan')) is None

    assert correct_hours_worked(24) is None
    assert correct_hours_worked(100) == 1.0
    assert correct_hours_worked(2400) == 24.0
