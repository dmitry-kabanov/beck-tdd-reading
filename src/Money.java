public class Money {

    protected int amount;

    protected String currency;

    Money(int amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    public boolean equals(Object obj) {
        Money money = (Money) obj;
        return (amount == money.amount) &&
                (currency.equals(money.currency()));
    }

    static Money dollar(int amount) {
        return new Dollar(amount, "USD");
    }

    static Money franc(int amount) {
        return new Franc(amount, "CHF");
    }

    /**
     * Multiply the amount by the multiplier.
     * @param multiplier Multiplier of the base amount
     * @return new Dollar object with multiplied amount
     */
    public Money times(int multiplier) {
        return new Money(this.amount * multiplier, currency);
    }

    String currency() {
        return this.currency;
    }

    public String toString() {
        return amount + " " + currency;
    }
}
