# Code Quest API

API documentation for the Code Quest project

# APIs

## GET /api/brands/

List all brands

Returns a list of all product brands




### Responses

#### 200



array







## POST /api/brands/

Create a new brand

Creates a new product brand




### Request Body

[Brand](#brand)







### Responses

#### 201



[Brand](#brand)







## GET /api/brands/{id}/

Get a specific brand



### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Responses

#### 200



[Brand](#brand)







## PATCH /api/brands/{id}/

Update a brand



### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Request Body

[PatchedBrand](#patchedbrand)







### Responses

#### 200



[Brand](#brand)







## DELETE /api/brands/{id}/

Delete a brand



### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Responses

#### 204


No response body




## GET /api/keywords/

List all keywords





### Responses

#### 200



array







## POST /api/keywords/

Create a new keyword





### Request Body

[Keyword](#keyword)







### Responses

#### 201



[Keyword](#keyword)







## GET /api/keywords/{id}/

Get a specific keyword



### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Responses

#### 200



[Keyword](#keyword)







## PATCH /api/keywords/{id}/

Update a keyword



### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Request Body

[PatchedKeyword](#patchedkeyword)







### Responses

#### 200



[Keyword](#keyword)







## DELETE /api/keywords/{id}/

Delete a keyword



### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Responses

#### 204


No response body




## GET /api/products/

List all products

Returns a list of all products with associated categories and keywords




### Responses

#### 200



array






Examples





```json
[
  {
    "id": "uuid-here",
    "arabic_name": "\u0645\u0646\u062a\u062c",
    "english_name": "Product",
    "nutrition_facts": {
      "calories": 200,
      "fat": "10g",
      "protein": "5g"
    },
    "brand": {
      "id": "uuid-here",
      "arabic_name": "\u0639\u0644\u0627\u0645\u0629 \u062a\u062c\u0627\u0631\u064a\u0629",
      "english_name": "Brand"
    },
    "keywords": [
      {
        "id": "uuid-here",
        "arabic_name": "\u0643\u0644\u0645\u0629 \u0645\u0641\u062a\u0627\u062d\u064a\u0629",
        "english_name": "Keyword"
      }
    ],
    "created_at": "2023-10-01T00:00:00Z",
    "updated_at": "2023-10-01T00:00:00Z"
  }
]
```



## POST /api/products/

Create a new product

Creates a new product with the provided data




### Request Body

[Product](#product)






Examples





```json
{
  "arabic_name": "\u0645\u0646\u062a\u062c",
  "english_name": "Product",
  "nutrition_facts": {
    "calories": 200,
    "fat": "10g",
    "protein": "5g"
  },
  "brand_id": "uuid-here",
  "keyword_ids": [
    "uuid-here"
  ]
}
```



### Responses

#### 201



[Product](#product)






Examples





```json
{
  "id": "uuid-here",
  "arabic_name": "\u0645\u0646\u062a\u062c",
  "english_name": "Product",
  "nutrition_facts": {
    "calories": 200,
    "fat": "10g",
    "protein": "5g"
  },
  "brand": {
    "id": "uuid-here",
    "arabic_name": "\u0639\u0644\u0627\u0645\u0629 \u062a\u062c\u0627\u0631\u064a\u0629",
    "english_name": "Brand"
  },
  "keywords": [
    {
      "id": "uuid-here",
      "arabic_name": "\u0643\u0644\u0645\u0629 \u0645\u0641\u062a\u0627\u062d\u064a\u0629",
      "english_name": "Keyword"
    }
  ],
  "created_at": "2023-10-01T00:00:00Z",
  "updated_at": "2023-10-01T00:00:00Z"
}
```



## GET /api/products/{id}/

Get a specific product

Returns details of a specific product by ID


### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Responses

#### 200



[Product](#product)






Examples





```json
{
  "id": "uuid-here",
  "arabic_name": "\u0645\u0646\u062a\u062c",
  "english_name": "Product",
  "nutrition_facts": {
    "calories": 200,
    "fat": "10g",
    "protein": "5g"
  },
  "brand": {
    "id": "uuid-here",
    "arabic_name": "\u0639\u0644\u0627\u0645\u0629 \u062a\u062c\u0627\u0631\u064a\u0629",
    "english_name": "Brand"
  },
  "keywords": [
    {
      "id": "uuid-here",
      "arabic_name": "\u0643\u0644\u0645\u0629 \u0645\u0641\u062a\u0627\u062d\u064a\u0629",
      "english_name": "Keyword"
    }
  ],
  "created_at": "2023-10-01T00:00:00Z",
  "updated_at": "2023-10-01T00:00:00Z"
}
```



## PATCH /api/products/{id}/

Update a product

Partially updates a product with the provided data, using optimistic locking


### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Request Body

[PatchedProduct](#patchedproduct)






Examples





```json
{
  "arabic_name": "\u0645\u0646\u062a\u062c",
  "english_name": "Product",
  "nutrition_facts": {
    "calories": 200,
    "fat": "10g",
    "protein": "5g"
  },
  "brand_id": "uuid-here",
  "keyword_ids": [
    "uuid-here"
  ]
}
```



### Responses

#### 200



[Product](#product)






Examples





```json
{
  "id": "uuid-here",
  "arabic_name": "\u0645\u0646\u062a\u062c",
  "english_name": "Product",
  "nutrition_facts": {
    "calories": 200,
    "fat": "10g",
    "protein": "5g"
  },
  "brand": {
    "id": "uuid-here",
    "arabic_name": "\u0639\u0644\u0627\u0645\u0629 \u062a\u062c\u0627\u0631\u064a\u0629",
    "english_name": "Brand"
  },
  "keywords": [
    {
      "id": "uuid-here",
      "arabic_name": "\u0643\u0644\u0645\u0629 \u0645\u0641\u062a\u0627\u062d\u064a\u0629",
      "english_name": "Keyword"
    }
  ],
  "created_at": "2023-10-01T00:00:00Z",
  "updated_at": "2023-10-01T00:00:00Z"
}
```



## DELETE /api/products/{id}/

Delete a product

Deletes a specific product by ID


### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Responses

#### 204


No response body




## GET /api/search/

Search for products

Searches products by query string, splitting into words and searching in Arabic or English fields based on language detection. Results are cached in Redis.


### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| page | integer |  | Page number for pagination. Default is 1. |
| page_size | integer |  | Number of results per page. Default is 20. |
| query | string | True | Search query string. Can contain multiple words to search for. |
| similarity_threshold | number |  | Threshold for similarity matching. Default is 0.3. |


### Responses

#### 200



array






Examples





```json
[
  {
    "id": "uuid-here",
    "arabic_name": "\u0645\u0646\u062a\u062c",
    "english_name": "Product",
    "nutrition_facts": {
      "calories": 200,
      "fat": "10g",
      "protein": "5g"
    },
    "brand": {
      "id": "uuid-here",
      "arabic_name": "\u0639\u0644\u0627\u0645\u0629 \u062a\u062c\u0627\u0631\u064a\u0629",
      "english_name": "Brand"
    },
    "keywords": [
      {
        "id": "uuid-here",
        "arabic_name": "\u0643\u0644\u0645\u0629 \u0645\u0641\u062a\u0627\u062d\u064a\u0629",
        "english_name": "Keyword"
      }
    ],
    "created_at": "2023-10-01T00:00:00Z",
    "updated_at": "2023-10-01T00:00:00Z"
  }
]
```



#### 400



object


| Field | Type | Description |
|-------|------|-------------|
| error | string |  |





#### 404



object


| Field | Type | Description |
|-------|------|-------------|
| error | string |  |





# Components



## Brand


Serializer for Brand model


| Field | Type | Description |
|-------|------|-------------|
| id | string |  |
| arabic_name | string |  |
| english_name | string |  |
| created_at | string |  |
| updated_at | string |  |


## Keyword


Serializer for Keyword model


| Field | Type | Description |
|-------|------|-------------|
| id | string |  |
| arabic_name | string |  |
| english_name | string |  |
| created_at | string |  |
| updated_at | string |  |


## PatchedBrand


Serializer for Brand model


| Field | Type | Description |
|-------|------|-------------|
| id | string |  |
| arabic_name | string |  |
| english_name | string |  |
| created_at | string |  |
| updated_at | string |  |


## PatchedKeyword


Serializer for Keyword model


| Field | Type | Description |
|-------|------|-------------|
| id | string |  |
| arabic_name | string |  |
| english_name | string |  |
| created_at | string |  |
| updated_at | string |  |


## PatchedProduct


Base serializer class.


| Field | Type | Description |
|-------|------|-------------|
| id | string |  |
| arabic_name | string |  |
| english_name | string |  |
| nutrition_facts |  |  |
| brand |  |  |
| brand_id | string |  |
| keywords | array |  |
| keyword_ids | array |  |
| created_at | string |  |
| updated_at | string |  |


## Product


Base serializer class.


| Field | Type | Description |
|-------|------|-------------|
| id | string |  |
| arabic_name | string |  |
| english_name | string |  |
| nutrition_facts |  |  |
| brand |  |  |
| brand_id | string |  |
| keywords | array |  |
| keyword_ids | array |  |
| created_at | string |  |
| updated_at | string |  |
