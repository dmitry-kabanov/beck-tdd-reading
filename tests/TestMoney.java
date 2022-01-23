import org.junit.Test;

import static org.junit.Assert.*;

public class TestMoney {
    @Test
    public void testEquality() {
        assertEquals(Money.dollar(5), new Dollar(5));
        assertNotEquals(Money.dollar(5), new Dollar(6));
        assertEquals(Money.franc(5), new Franc(5));
        assertNotEquals(Money.franc(5), new Franc(6));
        assertFalse(Money.franc(10).equals(Money.dollar(10)));
    }
}
