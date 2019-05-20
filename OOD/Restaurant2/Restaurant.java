// 题目：设计餐馆 II
// 不能订外卖
// 能预订座位
// MAX_DINETIME 为 2， 意为占用一桌吃饭的最大时长为2小时
// 如果餐桌被预定，则无法入座
// 餐馆的桌子有不同大小
// 餐馆会优先选择适合当前Party最小的空桌
// 相对设计餐馆 I，Table新增functions 需要实现。相关函数之后会调用restaurantDescription, 来验证你的程序是否正确。

class NoTableException extends Exception{

    public NoTableException(Party p)
	{
		super("No table available for party size: " + p.getSize());
	}
}

public class Restaurant {
	private List<Table> tables;
	private List<Meal> menu;
	public static final int MAX_DINEHOUR = 2;
	public static final long HOUR = 3600*1000;
	
	public Restaurant()
	{
		tables = new ArrayList<Table>();
		menu = new ArrayList<Meal>();
	}
	
	public void findTable(Party p) throws NoTableException
	{
		Date currentDate = new Date();
		for(Table t: tables)
		{
			if(t.isAvailable())
			{
				if(t.getCapacity() >= p.getSize())
				{
					if(t.noFollowReservation(currentDate))
					{
						t.markUnavailable();
						return;
					}
				}
			}
		}
		throw new NoTableException(p);
	}
	
	public void takeOrder(Table t, Order o)
	{
		t.setOrder(o);
	}
	
	public float checkOut(Table t)
	{
		float bill = 0;
		if(t.getCurrentOrder() != null)
		{
			bill = t.getCurrentOrder().getBill();
		}

		t.markAvailable();
		t.setOrder(null);
		
		return bill;
	}
	
	public List<Meal> getMenu()
	{
		return menu;
	}
	
	public void addTable(Table t)
	{
		tables.add(t);
		Collections.sort(tables);
	}
	
	public Reservation findTableForReservation(Party p, Date date)
	{
		for(Table table : tables)
		{
			if(table.getCapacity() >= p.getSize())
			{
				if(table.reserveForDate(date))
				{
					return new Reservation(table, date);
				}
			}
		}
		return null;
	}
	
	public void cancelReservation(Reservation r)
	{
		Date date = r.getDate();
		r.getTable().removeReservation(date);
	}
	
	public void redeemReservation(Reservation r)
	{
		Date date = r.getDate();
		Table table = r.getTable();
		
		table.markUnavailable();
		table.removeReservation(date);
	}
	
	public String restaurantDescription()
	{
		String description = "";
		for(int i = 0; i < tables.size(); i++)
		{
			Table table = tables.get(i);
			description += ("Table: " + table.getId() + ", table size: " + table.getCapacity() + ", isAvailable: " + table.isAvailable() + ".");
			if(table.getCurrentOrder() == null)
				description += " No current order for this table"; 
			else
				description +=  " Order price: " + table.getCurrentOrder().getBill();
			
			description += ". Current reservation dates for this table are: ";
			
			for(Date date : table.getReservation())
			{
				description += date.toGMTString() + " ; ";
			}
			
			description += ".\n";
		}
		description += "*****************************************\n";
		return description;
	}
}