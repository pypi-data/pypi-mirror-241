from django_actionable_messages.mixins import CardElement


class Section(CardElement):
    def __init__(self, start_group: bool = False, title: str = None, text: str = None, activity_image: str = None,
                 activity_title: str = None, activity_subtitle: str = None, activity_text: str = None, hero_image=None,
                 facts=None, actions=None, **kwargs) -> None:
        self._data = {}
        super().__init__(**kwargs)
        if start_group:
            self.set_start_group(start_group)
        if title is not None:
            self.set_title(title)
        if text is not None:
            self.set_text(text)
        if activity_image is not None:
            self.set_activity_image(activity_image)
        if activity_title is not None:
            self.set_activity_title(activity_title)
        if activity_subtitle is not None:
            self.set_activity_subtitle(activity_subtitle)
        if activity_text is not None:
            self.set_activity_text(activity_text)
        if hero_image is not None:
            self.set_hero_image(hero_image)
        if facts is not None:
            self.add_facts(facts)
        if actions is not None:
            self.add_potential_actions(actions)

    def set_start_group(self, start_group=True) -> None:
        self._data["startGroup"] = start_group

    def set_title(self, title) -> None:
        self._data["title"] = title

    def set_text(self, text) -> None:
        self._data["text"] = text

    def set_activity(self, image: str = None, title: str = None, subtitle: str = None, text: str = None) -> None:
        if image is not None:
            self.set_activity_image(image)
        if title is not None:
            self.set_activity_title(title)
        if subtitle is not None:
            self.set_activity_subtitle(subtitle)
        if text is not None:
            self.set_activity_text(text)

    def set_activity_image(self, image: str) -> None:
        self._data["activityImage"] = image

    def set_activity_title(self, title: str) -> None:
        self._data["activityTitle"] = title

    def set_activity_subtitle(self, subtitle: str) -> None:
        self._data["activitySubtitle"] = subtitle

    def set_activity_text(self, text: str) -> None:
        self._data["activityText"] = text

    def set_hero_image(self, hero_image) -> None:
        self._data["heroImage"] = hero_image.as_data()

    def add_facts(self, facts) -> None:
        self._data.setdefault("facts", [])
        if isinstance(facts, (list, set, tuple)):
            self._data["facts"].extend(self._get_items_list(facts))
        else:
            self._data["facts"].append(facts.as_data())

    def add_potential_actions(self, actions) -> None:
        self._data.setdefault("potentialAction", [])
        if isinstance(actions, (list, set, tuple)):
            self._data["potentialAction"].extend(self._get_items_list(actions))
        else:
            self._data["potentialAction"].append(actions.as_data())
