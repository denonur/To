        if message.lower().startswith("!switch") and await self.is_user_allowed(user):
            target_username = message.split("@")[-1].strip().lower()

            room_users = (await self.highrise.get_room_users()).content
            user_position = None
            for room_user, position in room_users:
                if room_user.id == user.id:
                    user_position = position
                    break
            if user_position is not None and isinstance(user_position, Position):
                target_user_position = None
                for room_user, position in room_users:
                    if room_user.username.lower() == target_username:
                        target_user_position = position
                        break
                if target_user_position is not None and isinstance(target_user_position, Position):
                    await self.teleport(room_user, user_position)
                    await self.teleport(user, target_user_position)