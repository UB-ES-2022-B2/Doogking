<template>
  <div class="grid">
    <div class="col-12">
        <DataView class="dataView" :value="products" :layout="layout" :paginator="true" :rows="9" :columns="4" :sortOrder="sortOrder" :sortField="sortField">
          <template #header>
            <div class="grid grid-nogutter">
              <div class="col-6 text-left">
                <Dropdown v-model="sortKey" :options="sortOptions" optionLabel="label" placeholder="Sort By Price" @change="onSortChange($event)"/>
              </div>
              <div class="col-6 text-right">
                <DataViewLayoutOptions v-model="layout" />
              </div>
            </div>
          </template>
          <template #list="slotProps">
            <div class="col-12">
              <div class="flex flex-column md:flex-row align-items-center p-3 w-full">
                <img src="@/assets/product/pexels-binyamin.jpg" :alt="slotProps.data.name" class="my-4 md:my-0 w-9 md:w-10rem shadow-2 mr-5" />
                <div class="flex-1 text-center md:text-left">
                  <div class="font-bold text-2xl">{{slotProps.data.name}}</div>
                  <div class="mb-3">{{slotProps.data.description}}</div>
                  <Rating :value="slotProps.data.rating" :stars="5" :readonly="true" :cancel="false" class="ui-rating" style="padding-bottom: 0.5em"></Rating>
                  <div class="flex align-items-center">
                    <Tag value="Host: Pedro" icon="pi pi-user" style="color: white; background-color: #6c757d"></Tag>
                  </div>

                </div>
                <div class="flex flex-row md:flex-column justify-content-between w-full md:w-auto align-items-center md:align-items-end mt-5 md:mt-0">
                  <span v-if="slotProps.data.favorite==true">
                      <Button id="favButtonList" icon="pi pi-heart-fill" @click="slotProps.data.favorite=false" class="p-button-rounded"/>
                  </span>
                  <span v-else>
                      <Button id="favButtonList" icon="pi pi-heart" @click="slotProps.data.favorite=true" class="p-button-rounded"/>
                  </span>
                  <span class="text-2xl font-semibold mb-2 align-self-center md:align-self-end">${{slotProps.data.price}}</span>
                  <Button label="View house" iconPos="right" class="buttonView"/>
                </div>
              </div>
            </div>
          </template>

          <template #grid="slotProps">
            <div class="col-12 md:col-4">
              <div class="card m-3 border-1 surface-border">
                <div class="flex align-items-center justify-content-between">
                  <div class="flex align-items-center">
                    <Tag value="Host: Pedro" icon="pi pi-user" style="color: white; background-color: #2A323D"></Tag>
                  </div>
                  <span v-if="slotProps.data.favorite==true">
                      <Button id="favButtonGrid" icon="pi pi-heart-fill" @click="slotProps.data.favorite=false" class="p-button-rounded"/>
                  </span>
                  <span v-else>
                      <Button id="favButtonGrid" icon="pi pi-heart" @click="slotProps.data.favorite=true" class="p-button-rounded"/>
                  </span>
                </div>
                <div class="text-center">
                  <img src="@/assets/product/pexels-binyamin.jpg" :alt="slotProps.data.name" class="w-9 shadow-2 my-3 mx-0"/>
                  <div class="text-2xl font-bold">{{slotProps.data.name}}</div>
                  <div class="mb-3">{{slotProps.data.description}}</div>
                  <Rating :value="slotProps.data.rating" :stars="5" :readonly="true" :cancel="false" class="ui-rating" style="padding-bottom: 0.5em"></Rating>
                </div>
                <div class="flex align-items-center justify-content-between">
                  <span class="text-2xl font-semibold">{{slotProps.data.price}}€ dia</span>
                  <Button label="View house" iconPos="right" class="buttonView"/>
                </div>
              </div>
            </div>
          </template>
        </DataView>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      products: [
        {
          'id': '1000',
          'code': 'f230fh0g3',
          'name': 'Bamboo Watch',
          'description': 'Product Description',
          'image': 'bamboo-watch.jpg',
          'price': 65,
          'favorite': true,
          'category': 'Accessories',
          'quantity': 24,
          'inventoryStatus': 'INSTOCK',
          'rating': 5
        },
        {
          'id': '1001',
          'code': 'nvklal433',
          'name': 'Black Watch',
          'description': 'Product Description',
          'image': 'black-watch.jpg',
          'price': 72,
          'favorite': true,
          'category': 'Accessories',
          'quantity': 61,
          'inventoryStatus': 'INSTOCK',
          'rating': 4
        },
        {
          'id': '1002',
          'code': 'zz21cz3c1',
          'name': 'Blue Band',
          'description': 'Product Description',
          'image': 'blue-band.jpg',
          'price': 79,
          'favorite': false,
          'category': 'Fitness',
          'quantity': 2,
          'inventoryStatus': 'LOWSTOCK',
          'rating': 3
        },
        {
          'id': '1003',
          'code': '244wgerg2',
          'name': 'Blue T-Shirt',
          'description': 'Product Description',
          'image': 'blue-t-shirt.jpg',
          'price': 29,
          'favorite': false,
          'category': 'Clothing',
          'quantity': 25,
          'inventoryStatus': 'INSTOCK',
          'rating': 5
        },
        {
          'id': '1004',
          'code': 'h456wer53',
          'name': 'Bracelet',
          'description': 'Product Description',
          'image': 'bracelet.jpg',
          'price': 15,
          'favorite': false,
          'category': 'Accessories',
          'quantity': 73,
          'inventoryStatus': 'INSTOCK',
          'rating': 4
        },
        {
          'id': '1005',
          'code': 'av2231fwg',
          'name': 'Brown Purse',
          'description': 'Product Description',
          'image': 'brown-purse.jpg',
          'price': 120,
          'favorite': false,
          'category': 'Accessories',
          'quantity': 0,
          'inventoryStatus': 'OUTOFSTOCK',
          'rating': 4
        },
        {
          'id': '1006',
          'code': 'bib36pfvm',
          'name': 'Chakra Bracelet',
          'description': 'Product Description',
          'image': 'chakra-bracelet.jpg',
          'price': 32,
          'favorite': false,
          'category': 'Accessories',
          'quantity': 5,
          'inventoryStatus': 'LOWSTOCK',
          'rating': 3
        },
        {
          'id': '1007',
          'code': 'mbvjkgip5',
          'name': 'Galaxy Earrings',
          'description': 'Product Description',
          'image': 'galaxy-earrings.jpg',
          'price': 34,
          'favorite': false,
          'category': 'Accessories',
          'quantity': 23,
          'inventoryStatus': 'INSTOCK',
          'rating': 5
        },
        {
          'id': '1008',
          'code': 'vbb124btr',
          'name': 'Game Controller',
          'description': 'Product Description',
          'image': 'game-controller.jpg',
          'price': 99,
          'favorite': false,
          'category': 'Electronics',
          'quantity': 2,
          'inventoryStatus': 'LOWSTOCK',
          'rating': 4
        },
        {
          'id': '1009',
          'code': 'cm230f032',
          'name': 'Gaming Set',
          'description': 'Product Description',
          'image': 'gaming-set.jpg',
          'price': 299,
          'favorite': false,
          'category': 'Electronics',
          'quantity': 63,
          'inventoryStatus': 'INSTOCK',
          'rating': 3
        },
        {
          'id': '1010',
          'code': 'plb34234v',
          'name': 'Gold Phone Case',
          'description': 'Product Description',
          'image': 'gold-phone-case.jpg',
          'price': 24,
          'favorite': false,
          'category': 'Accessories',
          'quantity': 0,
          'inventoryStatus': 'OUTOFSTOCK',
          'rating': 4
        },
        {
          'id': '1011',
          'code': '4920nnc2d',
          'name': 'Green Earbuds',
          'description': 'Product Description',
          'image': 'green-earbuds.jpg',
          'price': 89,
          'favorite': false,
          'category': 'Electronics',
          'quantity': 23,
          'inventoryStatus': 'INSTOCK',
          'rating': 4
        },
        {
          'id': '1012',
          'code': '250vm23cc',
          'name': 'Green T-Shirt',
          'description': 'Product Description',
          'image': 'green-t-shirt.jpg',
          'price': 49,
          'favorite': false,
          'category': 'Clothing',
          'quantity': 74,
          'inventoryStatus': 'INSTOCK',
          'rating': 5
        },
        {
          'id': '1013',
          'code': 'fldsmn31b',
          'name': 'Grey T-Shirt',
          'description': 'Product Description',
          'image': 'grey-t-shirt.jpg',
          'price': 48,
          'favorite': false,
          'category': 'Clothing',
          'quantity': 0,
          'inventoryStatus': 'OUTOFSTOCK',
          'rating': 3
        },
        {
          'id': '1014',
          'code': 'waas1x2as',
          'name': 'Headphones',
          'description': 'Product Description',
          'image': 'headphones.jpg',
          'price': 175,
          'favorite': false,
          'category': 'Electronics',
          'quantity': 8,
          'inventoryStatus': 'LOWSTOCK',
          'rating': 5
        },
        {
          'id': '1015',
          'code': 'vb34btbg5',
          'name': 'Light Green T-Shirt',
          'description': 'Product Description',
          'image': 'light-green-t-shirt.jpg',
          'price': 49,
          'favorite': false,
          'category': 'Clothing',
          'quantity': 34,
          'inventoryStatus': 'INSTOCK',
          'rating': 4
        },
        {
          'id': '1016',
          'code': 'k8l6j58jl',
          'name': 'Lime Band',
          'description': 'Product Description',
          'image': 'lime-band.jpg',
          'price': 79,
          'favorite': false,
          'category': 'Fitness',
          'quantity': 12,
          'inventoryStatus': 'INSTOCK',
          'rating': 3
        },
        {
          'id': '1017',
          'code': 'v435nn85n',
          'name': 'Mini Speakers',
          'description': 'Product Description',
          'image': 'mini-speakers.jpg',
          'price': 85,
          'favorite': false,
          'category': 'Clothing',
          'quantity': 42,
          'inventoryStatus': 'INSTOCK',
          'rating': 4
        },
        {
          'id': '1018',
          'code': '09zx9c0zc',
          'name': 'Painted Phone Case',
          'description': 'Product Description',
          'image': 'painted-phone-case.jpg',
          'price': 56,
          'favorite': false,
          'category': 'Accessories',
          'quantity': 41,
          'inventoryStatus': 'INSTOCK',
          'rating': 5
        },
        {
          'id': '1019',
          'code': 'mnb5mb2m5',
          'name': 'Pink Band',
          'description': 'Product Description',
          'image': 'pink-band.jpg',
          'price': 79,
          'favorite': false,
          'category': 'Fitness',
          'quantity': 63,
          'inventoryStatus': 'INSTOCK',
          'rating': 4
        },
        {
          'id': '1020',
          'code': 'r23fwf2w3',
          'name': 'Pink Purse',
          'description': 'Product Description',
          'image': 'pink-purse.jpg',
          'price': 110,
          'favorite': false,
          'category': 'Accessories',
          'quantity': 0,
          'inventoryStatus': 'OUTOFSTOCK',
          'rating': 4
        },
        {
          'id': '1021',
          'code': 'pxpzczo23',
          'name': 'Purple Band',
          'description': 'Product Description',
          'image': 'purple-band.jpg',
          'price': 79,
          'favorite': false,
          'category': 'Fitness',
          'quantity': 6,
          'inventoryStatus': 'LOWSTOCK',
          'rating': 3
        },
        {
          'id': '1022',
          'code': '2c42cb5cb',
          'name': 'Purple Gemstone Necklace',
          'description': 'Product Description',
          'image': 'purple-gemstone-necklace.jpg',
          'price': 45,
          'favorite': false,
          'category': 'Accessories',
          'quantity': 62,
          'inventoryStatus': 'INSTOCK',
          'rating': 4
        },
        {
          'id': '1023',
          'code': '5k43kkk23',
          'name': 'Purple T-Shirt',
          'description': 'Product Description',
          'image': 'purple-t-shirt.jpg',
          'price': 49,
          'favorite': false,
          'category': 'Clothing',
          'quantity': 2,
          'inventoryStatus': 'LOWSTOCK',
          'rating': 5
        },
        {
          'id': '1024',
          'code': 'lm2tny2k4',
          'name': 'Shoes',
          'description': 'Product Description',
          'image': 'shoes.jpg',
          'price': 64,
          'favorite': false,
          'category': 'Clothing',
          'quantity': 0,
          'inventoryStatus': 'INSTOCK',
          'rating': 4
        },
        {
          'id': '1025',
          'code': 'nbm5mv45n',
          'name': 'Sneakers',
          'description': 'Product Description',
          'image': 'sneakers.jpg',
          'price': 78,
          'favorite': false,
          'category': 'Clothing',
          'quantity': 52,
          'inventoryStatus': 'INSTOCK',
          'rating': 4
        },
        {
          'id': '1026',
          'code': 'zx23zc42c',
          'name': 'Teal T-Shirt',
          'description': 'Product Description',
          'image': 'teal-t-shirt.jpg',
          'price': 49,
          'favorite': false,
          'category': 'Clothing',
          'quantity': 3,
          'inventoryStatus': 'LOWSTOCK',
          'rating': 3
        },
        {
          'id': '1027',
          'code': 'acvx872gc',
          'name': 'Yellow Earbuds',
          'description': 'Product Description',
          'image': 'yellow-earbuds.jpg',
          'price': 89,
          'favorite': false,
          'category': 'Electronics',
          'quantity': 35,
          'inventoryStatus': 'INSTOCK',
          'rating': 3
        },
        {
          'id': '1028',
          'code': 'tx125ck42',
          'name': 'Yoga Mat',
          'description': 'Product Description',
          'image': 'yoga-mat.jpg',
          'price': 20,
          'favorite': false,
          'category': 'Fitness',
          'quantity': 15,
          'inventoryStatus': 'INSTOCK',
          'rating': 5
        },
        {
          'id': '1029',
          'code': 'gwuby345v',
          'name': 'Yoga Set',
          'description': 'Product Description',
          'image': 'yoga-set.jpg',
          'price': 20,
          'favorite': false,
          'category': 'Fitness',
          'quantity': 25,
          'inventoryStatus': 'INSTOCK',
          'rating': 8
        }
      ],
      layout: 'grid',
      sortKey: null,
      sortOrder: null,
      sortField: null,
      sortOptions: [
        {label: 'Price High to Low', value: '!price'},
        {label: 'Price Low to High', value: 'price'}
      ]
    }
  },
  created () {
  },
  methods: {
    onSortChange (event) {
      const value = event.value.value
      const sortValue = event.value

      if (value.indexOf('!') === 0) {
        this.sortOrder = -1
        this.sortField = value.substring(1, value.length)
        this.sortKey = sortValue
      } else {
        this.sortOrder = 1
        this.sortField = value
        this.sortKey = sortValue
      }
    },
    addFavorite (fav) {
      fav = true
    }
  }
}
</script>

<style scoped>

.col-12{
  padding-bottom: 0px;
}
.card {
  border-color: white;
  padding: 2rem;
  box-shadow: 0 2px 1px -1px white, 0 1px 1px 0 white, 0 1px 3px 0 white;
  border-radius: 3em;
  margin-bottom: 3rem;
  background: linear-gradient(
    to top,
    #2A323D 0%,
    #2A323D 74%,
    white 74%,
    white 75%,
    paleturquoise 75%,
    paleturquoise 100%
  );
}

.dataView >>> .p-dataViewGridItem {
  columns: 4;
}

.buttonView{
  background-color: #6c757d;
  border-color: #6c757d;
  color: white;
}

.buttonView:hover{
  background-color: #8DD0FF;
  border-color: #8DD0FF;
  outline-color: #8DD0FF;
  color: white;
}

.buttonView:focus {
  box-shadow: 0 0 0 0.1em #8DD0FF;
  background-color: #8DD0FF;
  border-color: #8DD0FF;
  outline-color: #8DD0FF;
  color: white;
}

.p-dropdown {
  width: 14rem;
  font-weight: normal;
}

.product-name {
  font-size: 1.5rem;
  font-weight: 700;
}

.product-description {
  margin: 0 0 1rem 0;
}

.ui-rating {
  color: yellow;
}

.product-category-icon {
  vertical-align: middle;
  margin-right: .5rem;
}

.product-category {
  font-weight: 600;
  vertical-align: middle;
}
#favButtonGrid{
  color: indianred;
  background-color: #2A323D;
  border-color: #2A323D;
}

#favButtonGrid:hover{
  color: indianred;
  background-color: #2A323D;
  border-color: #2A323D;
}

#favButtonGrid:focus{
  color: indianred;
  background-color: #2A323D;
  border-color: #2A323D;
  box-shadow: 0 0 0 0.1em indianred;
}

#favButtonList{
  color: indianred;
  background-color: #6c757d;
  border-color: #6c757d;
}

#favButtonList:hover{
  color: indianred;
  background-color: #6c757d;
  border-color: #6c757d;
}

#favButtonList:focus{
  color: indianred;
  background-color: #6c757d;
  border-color: #6c757d;
  outline-color: #6c757d;
  box-shadow: 0 0 0 0.1em indianred;
}
</style>
