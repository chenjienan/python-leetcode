class Reservation {
	private Table table;
	private Date date;
	
	public Reservation(Table table, Date date)
	{
		this.table = table;
		this.date = date;
	}
	
	public Date getDate()
	{
		return date;
	}
	
	public Table getTable()
	{
		return table;
	}
}