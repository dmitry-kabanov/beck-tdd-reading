import org.junit.Test;

import static org.junit.Assert.*;

public class TestDollar {
    @Test
    public void testMultiplication() {
        Money five = Money.dollar(5);
        assertEquals(Money.dollar(10), five.times(2));
        assertEquals(Money.dollar(15), five.times(3));
    }

    @Test
    public void testEquality() {
        assertEquals(Money.dollar(5), new Dollar(5));
        assertNotEquals(Money.dollar(5), new Dollar(6));
    }
}
