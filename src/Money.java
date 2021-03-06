public class Money implements Expression {

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
        return new Money(amount, "USD");
    }

    static Money franc(int amount) {
        return new Money(amount, "CHF");
    }

    /**
     * Multiply the amount by the multiplier.
     * @param multiplier Multiplier of the base amount
     * @return new Money object with multiplied amount
     */
    public Money times(int multiplier) {
        return new Money(amount * multiplier, currency);
    }

    public Expression plus(Expression addend) {
        return new Sum(this, addend);
    }

    public Money reduce(Bank bank, String to) {
        int rate = bank.rate(currency, to);
        return new Money(amount / rate, to);
    }

    String currency() {
        return this.currency;
    }

    public String toString() {
        return amount + " " + currency;
    }
}
