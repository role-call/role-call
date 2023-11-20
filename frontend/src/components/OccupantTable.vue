<template>
  <v-data-table-server
    v-model:items-per-page="itemsPerPage"
    :headers="headers"

    :items-length="itemsLength"
     :items="items"
    :loading="loading"
    class="elevation-1"
    item-value="name"
    :page="page"
    v-model:sort-by="sorting"
    @update:options="loadItems"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>My CRUD</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ props }">
            <v-btn
              color="primary"
              dark
              class="mb-2"
              v-bind="props"
            >
              New Item
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="8"
                    md="6"
                  >
                    <v-text-field
                      v-model="editedItem.firstName"
                      label="First name"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="8"
                    md="6"
                  >
                    <v-text-field
                      v-model="editedItem.lastName"
                      label="LastName"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >

                  </v-col>

                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue-darken-1"
                variant="text"
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue-darken-1"
                variant="text"
                @click="save"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue-darken-1" variant="text" @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
     <template v-slot:item.firstName="{ item }">
       <router-link :to="{name: 'main'}">{{item.firstName}}</router-link>
     </template>
        <template v-slot:item.actions="{ item }">
      <v-icon size="small" class="me-2"  @click="editItem(item)">
        mdi-pencil
      </v-icon>
      <v-icon size="small" > mdi-delete </v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn color="primary" > Reset </v-btn>
    </template>
  </v-data-table-server>
</template>


<script>
  import {useInstallationStore} from "@/store/installationstore";
  import {useTableStore} from "@/store/tablestore";
  import {mapState, storeToRefs} from "pinia";

  export default {
    name: "OccupantTable",
    data: () => ({
           dialog: false,
      dialogDelete: false,
      itemsPerPage: 2,
      headers: [
        {
          title: 'First Name',
          align: 'start',
          key: 'firstName',
        },
        { title: 'Last Name', key: 'lastName', align: 'end' },
        { title: 'Id', key: 'external_id', align: 'end' },
        { title: 'Actions', key: 'actions', sortable: false },
      ],
      loading: true,
      page:1,
      sorting:[],
      editedIndex: -1,
      editedItem: {
        firstName: '',
        lastName:'',
        external_id: '',
      },
      defaultItem: {
        firstName: '',
        lastName:'',
        external_id: '',
      },

    }),
    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      },
      ...mapState(useInstallationStore,{installation: 'chosenInstallation'}),
      ...mapState(useTableStore,['items','itemsLength'])
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
      installation(val) {


        this.page =1;
        this.loadItems();
      }
    },


    mounted() {

    },
    setup(props) {
      const tableStore = useTableStore();
      const installationStore = useInstallationStore();

      //installationStore.chosenInstallation = props.installation;
      return {installationStore, tableStore};
    },
    methods: {



      editItem (item) {
        this.editedIndex = this.items.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.items.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        this.items.splice(this.editedIndex, 1)
        this.closeDelete()
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.items[this.editedIndex], this.editedItem)
        } else {
          this.items.push(this.editedItem)
        }
        this.close()
      },

      async loadItems() {
        //console.log(params);
        this.loading = true

        var itemsPerPage = this.itemsPerPage;
        var page = this.page
        var queryparams = { page, itemsPerPage};

        if (this.sorting.length > 0) {
          queryparams.ordering = (this.sorting[0].order== "desc"?"-":"")+this.sorting[0].key;
        }
        await this.tableStore.getOccupants(this.installationStore.chosenInstallation,queryparams);

        this.loading = false

      },
    },
  }
</script>

