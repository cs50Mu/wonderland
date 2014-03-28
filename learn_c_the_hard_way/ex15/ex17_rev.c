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
	unsigned int max_data;
	unsigned int max_rows;
	struct Address *rows;
};

struct Connection {
	FILE *file;
	struct Database *db;
};

void die(const char *message, struct Connection *conn)
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

void Database_load(struct Connection *conn)
{
	int rc = fread(conn->db, sizeof(struct Database), 1, conn->file);
	if(rc != 1) die("Failed to load database.", conn);
}

struct Connection *Database_open(const char *filename, char mode, unsigned int max_data, unsigned int max_rows)
{
	struct Connection *conn = malloc(sizeof(struct Connection));
	if(!conn) die("Memory error!", conn);
	
	conn->db = malloc(sizeof(struct Database));
	if(!conn->db) die("Memory error!", conn);

	conn->db->rows = malloc(max_rows * sizeof(struct Address));
	if(!conn->db->rows) die("Memory error!", conn);

//	conn->db->rows->name = malloc(max_data * sizeof(char));
//	if(!conn->db->rows->name) die("Memory error!", conn);
//	
//	conn->db->rows->email = malloc(max_data * sizeof(char));
//	if(!conn->db->rows->email) die("Memory error!", conn);

	if(mode == 'c') {
		conn->file = fopen(filename, "w");
	} else {
		conn->file = fopen(filename, "r+");

		if(conn->file) {
			Database_load(conn);
		}
	}

	if(!conn->file) die("Failed to open the file", conn);

	return conn;
}

void Database_close(struct Connection *conn)
{
	if(conn) {
		if(conn->file) fclose(conn->file);
		if(conn->db) free(conn->db);
		free(conn);
	}
}

void Database_write(struct Connection *conn)
{
	rewind(conn->file);   // 使位置指针重新回到文件开头

	int rc = fwrite(conn->db, sizeof(struct Database), 1, conn->file);
	if(rc != 1) die("Failed to write database!", conn);

	rc = fflush(conn->file);
	if(rc == -1) die("Cannot flush database!", conn);
}

void Database_create(struct Connection *conn, unsigned int max_rows)
{
	int i = 0;

	for(i = 0; i < max_rows; i++) {
		// make a prototype to initialize it
		struct Address addr = {.id = i, .set = 0};
		// then just assign it
		conn->db->rows[i] = addr;
	}
}

void Database_set(struct Connection *conn, unsigned int max_data, int id, const char *name, const char *email)
{
	struct Address *addr = &conn->db->rows[id]; // bug 因为未检测id的范围，超出范围会segmentfault
	if (addr->set) die("Already set, delete it first!", conn);

	addr->set = 1;
	char *addr->name = malloc(sizeof(char) * max_data);
	char *addr->email = malloc(sizeof(char) * max_data);
	// fix this          若name太大超过了MAX_DATA，会导致addr->name缺失结束符
	char *res = strncpy(addr->name, name, max_data); // 
	// demonstrate the strncpy bug
	addr->name[max_data-1] = '\0';  // add '\0' manually, this should fix the bug 
	if (!res) die("Name copy failed", conn);

	res = strncpy(addr->email, email, max_data);
	addr->email[max_data-1] = '\0';  // add '\0' manually, this should fix the bug  
	if(!res) die("Email copy failed", conn);
}

void Database_get(struct Connection *conn, int id)
{
	struct Address *addr = &conn->db->rows[id];

	if(addr->set) {
		Address_print(addr);
	} else {
		die("Id is not set", conn);
	}
}

void Database_delete(struct Connection *conn, int id)
{
	struct Address addr = {.id = id, .set = 0};
	conn->db->rows[id] = addr;
}

void Database_list(struct Connection *conn, unsigned int max_rows)
{
	int i = 0;
	struct Database *db = conn->db;

	for(i=0; i < max_rows; i++) {
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

	int max_data = 512;
	int max_rows = 100;
	char *filename = argv[1];
	char action = argv[2][0];
	if(action == 'c') {
		max_data = atoi(argv[3]);
		max_rows = atoi(argv[4]);
	}
	struct Connection *conn = Database_open(filename, action, max_data, max_rows);
	int id = 0;

	if(argc > 3 && action != 'c') {
		id = atoi(argv[3]);  
		if(id >= max_rows) die("There's not that many records!", conn);
	}

	switch(action) {
		case 'c':
			Database_create(conn, max_rows);
			Database_write(conn);
			break;

		case 'g':
			if(argc != 4) die("Need an id to get", conn);

			Database_get(conn,id);
			break;

		case 's':
			if(argc != 6) die("Need id, name, email to set!", conn);

			Database_set(conn, max_data, id, argv[4], argv[5]);
			Database_write(conn);
			break;

		case 'd':
			if(argc != 4) die("Need id to delete!", conn);

			Database_delete(conn,id);
			Database_write(conn);
			break;

		case 'l':
			Database_list(conn, max_rows);
			break;

		default:
			die("Invalid action, only: c=create, g=get, s=set, d=del, l=list", conn);
	}

	Database_close(conn);

	return 0;
}
