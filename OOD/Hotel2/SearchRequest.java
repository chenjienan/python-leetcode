class SearchRequest {
	private Date startDate;
	private Date endDate;
	
	public SearchRequest(Date startDate, Date endDate) {
		// TODO Auto-generated constructor stub
		this.startDate = startDate;
		this.endDate = endDate;
	}
	
	public Date getStartDate()
	{
		return startDate;
	}
	
	public Date getEndDate()
	{
		return endDate;
	}
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		
		String res = "Start date is: " + startDate.toLocaleString() + ", End date is: " + endDate.toLocaleString();
		
		return res;
	}
	
	@Override
	public boolean equals(Object obj) {
		// TODO Auto-generated method stub
		if(obj == this) return true;
		if(!(obj instanceof SearchRequest)) return false;
		
		SearchRequest request = (SearchRequest) obj;
		
		return request.startDate == this.startDate && request.endDate == this.endDate;
	}
	
	@Override
	public int hashCode() {
		// TODO Auto-generated method stub
		int result = 17;
		result = 31 * result + startDate.hashCode();
		result = 31 * result + endDate.hashCode();
		return result;
	}
}