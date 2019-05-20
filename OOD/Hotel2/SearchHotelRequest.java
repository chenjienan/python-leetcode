class SearchHotelRequest {
	private Date startDate;
	private Date endDate;
	private int groupSize;
	
	public SearchHotelRequest(Date startDate, Date endDate, int groupSize)
	{
		this.startDate = startDate;
		this.endDate = endDate;
		this.groupSize = groupSize;
	}
	
	public Date getStartDate()
	{
		return startDate;
	}
	
	public Date getEndDate()
	{
		return endDate;
	}
	
	public int getGroupSize()
	{
		return groupSize;
	}
}