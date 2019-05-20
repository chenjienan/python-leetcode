// 设计一个可以打开三种文件格式的Kindle，文件格式分别为：PDF, MOBI , EPUB。

// 尝试使用 ENUM 处理文件格式。
// 尝试使用 simple factory 设计模式为每种格式创建用户。

import java.util.ArrayList;
import java.util.List;

public class Kindle {
    private List<Book> books;
	private EBookReaderFactory readerFactory;

	public Kindle() {
		books = new ArrayList<>();
		readerFactory = new EBookReaderFactory();
	}

	public String readBook(Book book) throws Exception {
		EBookReader reader = readerFactory.createReader(book);
		if (reader == null) {
			throw new Exception("Can't read this format");
		}
		return reader.displayReaderType() + ", book content is: " + reader.readBook();
	}

	public void downloadBook(Book b) {
		books.add(b);
	}

	public void uploadBook(Book b) {
		books.add(b);
	}

	public void deleteBook(Book b) {
		books.remove(b);
	}
}

enum Format {
	EPUB("epub"), PDF("pdf"), MOBI("mobi");

	private String content;

	Format(String content) {
		this.content = content;
	}

	public String getContent() {
		return content;
	}
}