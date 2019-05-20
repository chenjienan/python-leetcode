class Table implements Comparable<Table>{
	private int id;
	private int capacity;
	private boolean available;
	private Order order;
	List<Date> reservations;
	
	public Table(int id, int capacity)
	{
		this.id = id;
		this.capacity = capacity;
		available = true;
		order = null;
		reservations = new ArrayList<>();
	}
	
	public int getId()
	{
		return this.id;
	}
	
	public int getCapacity()
	{
		return this.capacity;
	}
	
	public List<Date> getReservation()
	{
		return reservations;
	}
	
	public boolean isAvailable()
	{
		return this.available;
	}
	
	public void markAvailable()
	{
		this.available = true;
	}
	
	public void markUnavailable()
	{
		this.available = false;
	}
	
	public Order getCurrentOrder()
	{
		return this.order;
	}
	
	public void setOrder(Order o)
	{
		if(order == null)
		{
			this.order = o;
		}
		else 
		{
			if(o != null)
			{
				this.order.mergeOrder(o);
			}
		}
	}

	@Override
	public int compareTo(Table compareTable) {
		// TODO Auto-generated method stub
		return this.capacity - compareTable.getCapacity();
	}
	
	private int findDatePosition(Date d)
	{
		int len = reservations.size();
		if(len == 0)
			return 0;
		if(d.getTime() > reservations.get(len - 1).getTime())
		{
	        return len;
	    }
	 
	    int i=0;
	    int j=len;
	 
	    while(i<j){
	        int m=(i+j)/2;
	        if(d.getTime() > reservations.get(m).getTime()){
	            i=m+1;
	        }else{
	            j=m;
	        }
	    }
	 
	    return j;
	}
	
	public boolean noFollowReservation(Date d)
	{
		final int MILLI_TO_HOUR = 1000 * 60 * 60;
		int position = findDatePosition(d);
		
		if(position < reservations.size())
		{
			Date nextReservation = reservations.get(position);
			int diff = (int) ((nextReservation.getTime() - d.getTime()) / MILLI_TO_HOUR);
			if(diff < Restaurant.MAX_DINEHOUR)
			{
				return false;
			}
		}
		return true;
	}
	
	public boolean reserveForDate(Date d)
	{
		final int MILLI_TO_HOUR = 1000 * 60 * 60;
		int position = findDatePosition(d);
		int before = position - 1;
		int after = position;
		
		if(before >= 0)
		{
			Date previousReservation = reservations.get(before);
			int diff = (int) ((d.getTime() - previousReservation.getTime()) / MILLI_TO_HOUR);
			if(diff < Restaurant.MAX_DINEHOUR)
			{
				return false;
			}
		}
		
		if(after < reservations.size())
		{
			Date nextReservation = reservations.get(after);
			int diff = (int) ((nextReservation.getTime() - d.getTime()) / MILLI_TO_HOUR);
			if(diff < Restaurant.MAX_DINEHOUR)
			{
				return false;
			}
		}
		
		reservations.add(position, d);
		return true;
	}
	
	public void removeReservation(Date d)
	{
		reservations.remove(d);
	}
}