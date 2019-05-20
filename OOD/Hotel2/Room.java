class Room {
    public static final int DAY = 1*24*60*60*1000;
    
	private int id;
	private RoomType roomType;
	private Set<Date> reservations;
	
	public Room(int id, RoomType roomType)
	{
		this.id = id;
		this.roomType = roomType;
		reservations = new HashSet<Date>();
	}
	
	public boolean isValidRequest(SearchRequest request)
	{
		Date date = new Date(request.getStartDate().getTime());
		for (; date.before(request.getEndDate()); date.setTime(date.getTime() + DAY))
		{
			Date tempDate = new Date(date.getTime());
			if(reservations.contains(tempDate))
			{
				return false;
			}
		}
		return true;
	}
	
	public void makeReservation(Date startDate, Date endDate)
	{
		Date date = new Date(startDate.getTime());
		for (; date.before(endDate); date.setTime(date.getTime() + DAY))
		{
			Date tempDate = new Date(date.getTime());
			reservations.add(tempDate);
		}
	}
	
	public void cancelReservation(Reservation reservation)
	{
		Date date = new Date(reservation.getStartDate().getTime());
		for (; date.before(reservation.getEndDate()); date.setTime(date.getTime() + DAY))
		{
			Date tempDate = new Date(date.getTime());
			reservations.remove(tempDate);
		}
	}
	
	public RoomType getRoomType()
	{
		return roomType;
	}
	
	public int getId()
	{
		return this.id;
	}
}