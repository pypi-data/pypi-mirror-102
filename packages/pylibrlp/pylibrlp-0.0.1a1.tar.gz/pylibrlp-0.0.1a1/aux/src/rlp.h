#ifndef RLP_T_
#define RLP_T_

#include <stdlib.h>

#ifndef RLP_MAX_LIST_DEPTH
#define RLP_MAX_LIST_DEPTH 1024
#endif

#define RLP_SUCCESS 0
#define RLP_FAILURE -1


enum rlp_state {
	RLP_DECODE,
	RLP_ENCODE,
	RLP_LIST_ASCEND,
	RLP_LIST_DESCEND,
	RLP_STRING,
	RLP_END,
};


typedef struct rlp_encoder {
	char *buf;
	char alloc;
	int depth;
	int size;
	enum rlp_state state;
	char *list_ptr[RLP_MAX_LIST_DEPTH];
	char *ptr;
} rlp_encoder_t;


int rlp_init(rlp_encoder_t *encoder, int buffer_capacity, char *content);
void rlp_free(rlp_encoder_t *encoder);

// encode
int rlp_descend(rlp_encoder_t *encoder);
int rlp_ascend(rlp_encoder_t *encoder);
int rlp_add(rlp_encoder_t *encoder, int len, const char *data);

// decode
int rlp_next(rlp_encoder_t *encoder, int *zl, char **zdest);

#endif
