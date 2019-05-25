public class BookingSystem {
    private List<Hotel> hotels;
	
	public BookingSystem()
	{
		hotels = new ArrayList<>();
	}
	
	public List<Hotel> searchHotel(SearchHotelRequest request)
	{
		List<Hotel> availableHotels = new ArrayList<>();
		for(Hotel hotel : hotels)
		{	
			// Create a new search
			SearchRequest searchRequest = new SearchRequest(request.getStartDate(), request.getEndDate());
			Map<RoomType, List<Room>> searchRes = hotel.handleSearchResult(searchRequest);
			int availableCapacity = 0;
			for(Entry<RoomType, List<Room>> entry : searchRes.entrySet())
			{
				availableCapacity += entry.getKey().getCapacity() * entry.getValue().size();
			}
			if(availableCapacity >= request.getGroupSize())
			{
				availableHotels.add(hotel);
			}
		}
		return availableHotels;
	}
	
	public Reservation makeReservation(Hotel hotel, ReservationRequest request)
	{
		return hotel.makeReservation(request);
	}
	
	public void cancelReservation(Reservation reservation)
	{
		reservation.getHotel().cancelReservation(reservation);
	}
	
	public List<Hotel> getHotels()
	{
		return hotels;
	}
}