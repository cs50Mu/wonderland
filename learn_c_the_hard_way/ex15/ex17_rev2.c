#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>


struct Address {
	int id;
	int set;
	char *name;
	char *email;
};

struct Database {
	struct Address *rows;   // 指向结构体数组的指针
	int max_data;
	int max_rows;
};

struct Connection {
	FILE *file;
	struct Database *db;
};

static struct Connection *conn;    // 设为全局性的

void die(const char *message)
{
	if (errno) {
		perror(message);
	} else {
		printf("ERROR: %s\n", message);
	}
	
	if(conn) {                    //  when error occurs, clean it up before exit
		if(conn->file) fclose(conn->file);
		if(conn->db) free(conn->db);
		free(conn);
	}

	exit(1);
}

void Address_print(struct Address *addr)
{
	printf("%d %s %s\n",\
			addr->id, addr->name, addr->email);
}

void Database_load(void)
{
	struct Address *addr;

	if(fread(&conn->db->max_data, sizeof(conn->db->max_data), 1, conn->file) != 1)
		die("Failed to load database!");
	if(fread(&conn->db->max_rows, sizeof(conn->db->max_rows), 1, conn->file) != 1)
		die("Failed to load database!");

	conn->db->rows = malloc(conn->db->max_rows * sizeof(struct Address));
	if(!conn->db->rows) die("Memory error!");
	for(addr = conn->db->rows; addr < conn->db->rows + conn->db->max_rows; addr++) {
		if(fread(&addr->id, sizeof(addr->id), 1, conn->file) != 1 ||\
				fread(&addr->set, sizeof(addr->set), 1, conn->file) != 1)
			die("Failed to load database!");

		addr->name = malloc(conn->db->max_data * sizeof(char));
		addr->email = malloc(conn->db->max_data * sizeof(char));
		if(fread(addr->name, sizeof(addr->name), 1, conn->file) != 1 ||\
			       fread(addr->email, sizeof(addr->email), 1, conn->file) != 1)
			die("Failed to load database!");
	}
}	


void Database_open(const char *filename, char mode)
{
	conn = malloc(sizeof(struct Connection));
	if(!conn) die("Memory error!");
	
	conn->db = malloc(sizeof(struct Database));
	if(!conn->db) die("Memory error!");

	if(mode == 'c') {
		conn->file = fopen(filename, "w");
	} else {
		conn->file = fopen(filename, "r+");

		if(conn->file) {
			Database_load();
		}
	}

	if(!conn->file) die("Failed to open the file");

}

void Database_close(void)
{
	if(conn) {
		if(conn->file) fclose(conn->file);
		if(conn->db) free(conn->db);
		free(conn);
	}
}

void Database_write(void)
{
	rewind(conn->file);   // 使位置指针重新回到文件开头
	int max_data = conn->db->max_data;
	int max_rows = conn->db->max_rows;
	struct Address *addr;

	if(fwrite(&max_data, sizeof(max_data), 1, conn->file) != 1 ||\
			fwrite(&max_rows, sizeof(max_data), 1, conn->file) != 1)
		die("Failed to write database!");

	for(addr = conn->db->rows; addr < conn->db->rows + max_rows; addr++) {
		if(fwrite(&addr->id, sizeof(addr->id), 1, conn->file) != 1 ||\
				fwrite(&addr->set, sizeof(addr->set), 1, conn->file) != 1 ||\
				fwrite(addr->name, max_data * sizeof(char), 1, conn->file) != 1 ||\
				fwrite(addr->name, max_data * sizeof(char), 1, conn->file) != 1) 
			die("Failed to write database!");

	if(fflush(conn->file) == -1)  die("Cannot flush database!");
}
}

void Database_create(void)
{
	int i = 0;
	struct Address *addr;
	int max_data = conn->db->max_data;
	int max_rows = conn->db->max_rows;
	conn->db->rows = malloc(max_rows * sizeof(struct Address));
	if(!conn->db->rows) die("Memory error!");

	for(i = 0; i < max_rows; i++) {
		addr = &conn->db->rows[i];
		addr->id = i;
		addr->set = 0;

		addr->name = malloc(max_data * sizeof(char));
		if(!addr->name) die("Memory error!");

		addr->email = malloc(max_data * sizeof(char));
		if(!addr->email) die("Memory error!");
	}
}

void Database_set(int id, const char *name, const char *email)
{
	struct Address *addr = &conn->db->rows[id]; // bug 因为未检测id的范围，超出范围会segmentfault
	int max_data = conn->db->max_data;
	if (addr->set) die("Already set, delete it first!");

	addr->set = 1;
	addr->name = malloc(max_data * sizeof(char)); // 使用前要先分配内存，切记！
	addr->email = malloc(max_data * sizeof(char));
	// fix this          若name太大超过了MAX_DATA，会导致addr->name缺失结束符
	char *res = strncpy(addr->name, name, max_data); // 
	// demonstrate the strncpy bug
	addr->name[max_data-1] = '\0';  // add '\0' manually, this should fix the bug 
	if (!res) die("Name copy failed");

	res = strncpy(addr->email, email, max_data);
	addr->email[max_data-1] = '\0';  // add '\0' manually, this should fix the bug  
	if(!res) die("Email copy failed");
}

void Database_get(int id)
{
	struct Address *addr = &conn->db->rows[id];

	if(addr->set) {
		Address_print(addr);
	} else {
		die("Id is not set");
	}
}

void Database_delete(int id)
{
	struct Address addr = {.id = id, .set = 0};
	conn->db->rows[id] = addr;
}

void Database_list(void)
{
	int i = 0;
	struct Database *db = conn->db;

	for(i=0; i < conn->db->max_rows; i++) {
		struct Address *cur = &db->rows[i];

		if(cur->set) {
			Address_print(cur);
		}
	}
}

int main(int argc, char *argv[])
{
	if(argc < 3) {
		printf("USAGE: ex17 <dbfile> <action> [action params]\n");
		exit(1);
	}

	char *filename = argv[1];
	char action = argv[2][0];
	Database_open(filename, action);
	int id = 0;

	if(argc > 3 && action != 'c') {
		id = atoi(argv[3]);  
		if(id >= conn->db->max_rows) die("There's not that many records!");
	}

	switch(action) {
		case 'c':
			if(argc != 5) die("USAGE: ex17 <dbfile> c max_data max_rows");
			conn->db->max_data = atoi(argv[3]);
			conn->db->max_rows = atoi(argv[4]);
			Database_create();
			Database_write();
			break;

		case 'g':
			if(argc != 4) die("Need an id to get");

			Database_get(id);
			break;

		case 's':
			if(argc != 6) die("Need id, name, email to set!");

			Database_set(id, argv[4], argv[5]);
			Database_write();
			break;

		case 'd':
			if(argc != 4) die("Need id to delete!");

			Database_delete(id);
			Database_write();
			break;

		case 'l':
			Database_list();
			break;

		default:
			die("Invalid action, only: c=create, g=get, s=set, d=del, l=list");
	}

	Database_close();

	return 0;
}
