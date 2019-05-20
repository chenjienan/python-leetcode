// 设计一个自动咖啡机，加入一袋咖啡包，简单地煮一杯咖啡。

// 每个咖啡包包含有咖啡的配方，如加入了多少牛奶，或加入了多少糖
// 咖啡机可根据咖啡包提供的配方制作咖啡
// 只考虑两种成分成分：糖（sugar）和牛奶（milk）
// 普通咖啡的成本是2元。 加入一份牛奶或糖会使成本增加0.5元
// 考虑使用Decorator Design Pattern

public class CoffeeMaker {

    public Coffee makeCoffee(CoffeePack pack) {
		Coffee coffee = new SimpleCoffee();

		for (int i = 0; i < pack.getNeededMilk(); i++) {
			coffee = new WithMilk(coffee);
		}

		for (int i = 0; i < pack.getNeededSugar(); i++) {
			coffee = new WithSugar(coffee);
		}

		return coffee;
	}
}