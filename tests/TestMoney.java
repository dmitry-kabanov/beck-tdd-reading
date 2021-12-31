import org.junit.Test;

import static org.junit.Assert.assertFalse;

public class TestMoney {
    @Test
    public void testEquality() {
        assertFalse(new Franc(10).equals(new Dollar(10)));
    }
}
