package com.example.catpet;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;
public class ContactAdapter extends RecyclerView.Adapter<ContactAdapter.ContactViewHolder> {

    private List<ContactItem> items;

    public ContactAdapter(List<ContactItem> items) {
        this.items = items;
    }

    @NonNull
    @Override
    public ContactViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_contact, parent, false);
        return new ContactViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ContactViewHolder holder, int position) {
        ContactItem item = items.get(position);
        holder.nombre.setText(item.getNombre());
        holder.info.setText(item.getInfo());
        holder.imagen.setImageResource(item.getImagenResId());
    }

    @Override
    public int getItemCount() {
        return items.size();
    }

    static class ContactViewHolder extends RecyclerView.ViewHolder {
        TextView nombre, info;
        ImageView imagen;

        public ContactViewHolder(@NonNull View itemView) {
            super(itemView);
            nombre = itemView.findViewById(R.id.txt_contact_name);
            info = itemView.findViewById(R.id.txt_contact_info);
            imagen = itemView.findViewById(R.id.img_contact);
        }
    }
}
