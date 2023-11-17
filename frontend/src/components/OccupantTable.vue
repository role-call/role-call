<template>
  <v-data-table
    v-model:items-per-page="itemsPerPage"
    :headers="headers"
    :items-length="totalItems"
    :items="tableStore.items"
    :loading="loading"
    class="elevation-1"
    item-value="name"
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
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.firstName"
                      label="First name"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
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
  </v-data-table>
</template>

<script>
  import {useInstallationStore} from "@/store/installationstore";
  import {useTableStore} from "@/store/tablestore";

  export default {
    name: "OccupantTable",
    props: ["installation"],
    data: () => ({
           dialog: false,
      dialogDelete: false,
      itemsPerPage: 5,
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
      serverItems: [],
      loading: true,
      totalItems: 0,
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
      }
    }),
    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },


    mounted() {
      this.initialize();

    },
    setup(props) {
      const tableStore = useTableStore();
      const installationStore = useInstallationStore();
      installationStore.chosenInstallation = props.installation;
      return {installationStore, tableStore};
    },
    methods: {
      initialize() {
        this.loadItems({ page:0, itemsPerPage:1, sortBy:"firstName" });
      },
      editItem (item) {
        this.editedIndex = this.serverItems.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.serverItems.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        this.serverItems.splice(this.editedIndex, 1)
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
          Object.assign(this.serverItems[this.editedIndex], this.editedItem)
        } else {
          this.serverItems.push(this.editedItem)
        }
        this.close()
      },

      async loadItems({ page, itemsPerPage, sortBy }) {
        this.loading = true
        await this.installationStore.getOccupants();
        this.tableStore.items = this.installationStore.occupants
        this.totalItems = 100
        this.loading = false

      },
    },
  }
</script>

