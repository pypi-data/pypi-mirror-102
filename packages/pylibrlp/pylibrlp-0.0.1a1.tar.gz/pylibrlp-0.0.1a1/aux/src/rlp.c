#include <stdlib.h>

#include "rlp.h"

int rlp_init(rlp_encoder_t *encoder, int buffer_capacity, char *content) {
	encoder->depth = 0;
	if (content != NULL) {
		encoder->buf = content;
		encoder->alloc = 0;
		encoder->state = RLP_DECODE;
		encoder->size = buffer_capacity;
		encoder->ptr = encoder->buf;
		encoder->list_ptr[0] = encoder->buf + buffer_capacity;
 	} else {
		encoder->buf = malloc(buffer_capacity);
		encoder->alloc = 1;
		encoder->state = RLP_ENCODE;
		encoder->size = 0;
		encoder->ptr = encoder->buf;
	}
}

void rlp_free(rlp_encoder_t *encoder) {
	if (encoder->alloc) {
		free(encoder->buf);
	}
	encoder->ptr = NULL;
}

//int rlp_get(rlp_encoder_t *encoder, int *zl, char **zdest) {
//	*zdest = encoder->buf;
//	*zl = encoder->size;
//	return 0;
//}
