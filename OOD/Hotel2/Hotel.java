// 题目：设计Booking System
// 目前系统里有两家Hotel
// Hotel目前有两种房间类型：SINGLE和DOUBLE
// Booking System能够支持搜索，输入日期 和 人数， 能够返回住得下
// 的Hotels
// 能够支持预定
// 能够取消预定
// 需要实现BookingSystem class

import java.util.Map.Entry;

class Hotel {
    public static final int DAY = 1*24*60*60*1000;
    
	private int id;
	private List<Room> rooms;
	private LRUCache cache;
	
	public Hotel(int id)
	{
		this.id = id;
		cache = new LRUCache(2);
		rooms = new ArrayList<>();
	}
	
	public int getId()
	{
		return this.id;
	}
	
	public Reservation makeReservation(ReservationRequest request)
	{
		Reservation reservation = new Reservation(request.getStartDate(), request.getEndDate());
		
		SearchRequest search = new SearchRequest(request.getStartDate(), request.getEndDate());
		
		Map<RoomType, List<Room>> roomsAvailable = getAvailableRooms(search);
		
		Map<RoomType, Integer> roomsNeeded = request.getRoomsNeeded();
		
		for(Entry<RoomType, Integer> entry : roomsNeeded.entrySet())
		{
			RoomType roomType = entry.getKey();
			int roomCount = entry.getValue();
			
			List<Room> rooms = roomsAvailable.get(roomType);
			
			//Not enough rooms
			if(entry.getValue() > rooms.size())
			{
				cache.put(search, roomsAvailable);
				return null;
			}
			
			for(int i = 0; i < roomCount; i++)
			{	
				Room room = rooms.remove(0);
				reservation.getRooms().add(room);
			}
			
			roomsAvailable.put(entry.getKey(), rooms);
		}
		
		cache.put(search, roomsAvailable);
		
		for(Room room : reservation.getRooms())
		{
			room.makeReservation(reservation.getStartDate(), reservation.getEndDate());
		}
		
		return reservation;
	}
	
	public Map<RoomType, List<Room>> handleSearchResult(SearchRequest request)
	{
		if(cache.containsKey(request))
		{
			return cache.get(request);
		}
		
		Map<RoomType, List<Room>> res = getAvailableRooms(request);
		
		cache.put(request, res);
		
		return res;
	}
	
	public void cancelReservation(Reservation reservation)
	{
		for(Room room : reservation.getRooms())
		{
			room.cancelReservation(reservation);
		}
	}
	
	public List<Room> getRooms()
	{
		return rooms;
	}
	
	private Map<RoomType, List<Room>> getAvailableRooms(SearchRequest request)
	{
		Map<RoomType, List<Room>> res = new HashMap<>();
		
		res.put(RoomType.SINGLE, new ArrayList<>());
		res.put(RoomType.DOUBLE, new ArrayList<>());
		
		for(Room room : rooms)
		{
			if(room.isValidRequest(request))
			{
				List<Room> roomList = res.get(room.getRoomType());
				roomList.add(room);
				res.put(room.getRoomType(), roomList);
			}
		}
		
		return res;
	}
	
	public String printCache()
	{
		return "Hotel Id: " + getId() + "\nPrinting Cache ...\n" + cache.toString() +
    		   "*****************************\n";
	}
}

class LRUCache extends LinkedHashMap<SearchRequest, Map<RoomType, List<Room>>>{

	private static final long serialVersionUID = 1L;
	private int capacity;
	
	public LRUCache(int capacity)
	{
		super(capacity);
		this.capacity = capacity;
	}
	
	@Override
	protected boolean removeEldestEntry(Entry<SearchRequest, Map<RoomType, List<Room>>> eldest) {
		// TODO Auto-generated method stub
		return size() > this.capacity;
	}
	
	private String printAvailableRooms(Map<RoomType, List<Room>> rooms)
	{
		String res = "";
		for(Entry<RoomType, List<Room>> entry : rooms.entrySet())
		{
			res += "For room type: " + entry.getKey() + ", available rooms are: ";
			for(Room room : entry.getValue())
			{
				res += room.getId() + "; ";
			}
			res += ". ";
		}
		return res;
	}
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		
		String res = "";
		
		for(Entry<SearchRequest, Map<RoomType, List<Room>>> entry : super.entrySet())
		{
			res += ("Search Request -> " + entry.getKey().toString() + "\n");
			res += ("Value -> " + printAvailableRooms(entry.getValue()) + "\n");
			res += "\n";
		}

		return res;
	}
}

enum RoomType {
	SINGLE(1),
	DOUBLE(2);
	
	private int capacity;
	
	RoomType(int capacity)
	{
		this.capacity = capacity;
	}
	
	public int getCapacity() {
		return capacity;
	}
}
